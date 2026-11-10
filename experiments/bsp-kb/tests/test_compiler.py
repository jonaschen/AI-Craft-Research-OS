import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from bsp_kb.__main__ import ROOT
from bsp_kb.compiler import check_views, compile_views, digest, render_views


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / 'corpus'
        self.root.mkdir()
        for name in ('content', 'evaluation', 'templates'):
            shutil.copytree(ROOT / name, self.root / name)
        for name in ('entries.json', 'sources.json'):
            shutil.copy(ROOT / name, self.root / name)
        self.output = self.base / 'bundle'

    def change_entries(self, fn):
        path = self.root / 'entries.json'
        entries = json.loads(path.read_text())
        fn(entries)
        path.write_text(json.dumps(entries, ensure_ascii=False))

    def test_reproducible_across_directories(self):
        one = compile_views(self.root, self.output)
        other_root = self.base / 'copy'
        shutil.copytree(self.root, other_root)
        two = compile_views(other_root, self.base / 'other-bundle')
        self.assertEqual(one['bundle_sha256'], two['bundle_sha256'])
        self.assertEqual(one['revision'], two['revision'])
        for path in self.output.rglob('*'):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (self.base / 'other-bundle' / path.relative_to(self.output)).read_bytes())
        self.assertTrue(check_views(self.root, self.output)['valid'])

    def test_human_and_agent_use_same_content_and_fingerprint(self):
        compile_views(self.root, self.output)
        index = json.loads((self.output / 'agent/index.json').read_text())
        rows = [json.loads(line) for line in (self.output / 'agent/context.jsonl').read_text().splitlines()]
        self.assertEqual(index['chunks'], rows)
        for row in rows:
            self.assertEqual(row['content_sha256'], digest((self.root / row['canonical_path']).read_bytes()))
            self.assertIn(row['text'], (self.output / row['path']).read_text())
            skill_ref = self.output / f"skills/bsp-knowledge/references/{row['entry_id']}.md"
            self.assertIn(row['text'], skill_ref.read_text())

    def test_manifest_detects_source_and_output_drift(self):
        compile_views(self.root, self.output)
        source = self.root / 'content/boot.md'
        source.write_text(source.read_text() + '\nNew evidence.\n')
        result = check_views(self.root, self.output)
        self.assertFalse(result['valid'])
        self.assertIn('manifest.json', result['changed'])
        self.assertIn('human/explanation/boot.md', result['changed'])
        self.assertIn('agent/context.jsonl', result['changed'])
        self.assertIn('skills/bsp-knowledge/references/boot.md', result['changed'])

    def test_evaluation_and_unregistered_content_never_exported(self):
        before = render_views(self.root)
        (self.root / 'evaluation/secret.md').write_text('ORACLE_SECRET')
        (self.root / 'content/unregistered.md').write_text('UNREGISTERED_SECRET')
        self.assertEqual(before, render_views(self.root))
        self.assertNotIn(b'ORACLE_SECRET', b''.join(before.values()))

    def test_template_changes_invalidate_bundle(self):
        compile_views(self.root, self.output)
        template = self.root / 'templates/bsp-knowledge/SKILL.md'
        template.write_text(template.read_text() + '\nAdditional routing.\n')
        result = check_views(self.root, self.output)
        self.assertFalse(result['valid'])
        self.assertIn('skills/bsp-knowledge/SKILL.md', result['changed'])

    def test_existing_output_is_preserved(self):
        self.output.mkdir()
        marker = self.output / 'personal.txt'
        marker.write_text('keep')
        with self.assertRaises(ValueError):
            compile_views(self.root, self.output)
        self.assertEqual(marker.read_text(), 'keep')

    def test_source_locations_and_symlinks_are_rejected(self):
        for output in (self.root, self.base, self.root / 'content/new', self.root / 'evaluation/new'):
            with self.subTest(output=output), self.assertRaises(ValueError):
                compile_views(self.root, output)
        self.output.symlink_to(self.base / 'nonexistent', target_is_directory=True)
        with self.assertRaises(ValueError):
            compile_views(self.root, self.output)

    def test_bundle_tamper_missing_extra_and_symlink(self):
        compile_views(self.root, self.output)
        (self.output / 'llms.txt').write_text('tampered')
        (self.output / 'agent/index.json').unlink()
        (self.output / 'extra.txt').write_text('extra')
        (self.output / 'external').symlink_to(self.root, target_is_directory=True)
        result = check_views(self.root, self.output)
        self.assertFalse(result['valid'])
        self.assertEqual(result['changed'], ['llms.txt'])
        self.assertEqual(result['missing'], ['agent/index.json'])
        self.assertEqual(result['unexpected'], ['extra.txt'])
        self.assertEqual(result['invalid_paths'], ['external'])

    def test_missing_bundle(self):
        result = check_views(self.root, self.output)
        self.assertFalse(result['valid'])
        self.assertIn('manifest.json', result['missing'])
        self.assertFalse(self.output.exists())

    def test_categories_and_internal_links_remain_portable(self):
        self.change_entries(lambda entries: entries[0].update(diataxis='reference'))
        path = self.root / 'content/boot.md'
        path.write_text(path.read_text() + '\n[組成](bsp.md#overview)\n')
        compile_views(self.root, self.output)
        self.assertIn('(../reference/bsp.md#overview)', (self.output / 'human/explanation/boot.md').read_text())
        self.assertIn('(bsp.md#overview)', (self.output / 'skills/bsp-knowledge/references/boot.md').read_text())
        chunks = json.loads((self.output / 'agent/index.json').read_text())['chunks']
        self.assertTrue(any('(../reference/bsp.md#overview)' in chunk['text'] for chunk in chunks))
        # Copy ONLY the skill to a new location and validate its local references.
        skill = self.base / 'installed-skill'
        shutil.copytree(self.output / 'skills/bsp-knowledge', skill)
        for path in skill.rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
                if not target.startswith(('https://', 'http://', '#')):
                    linked = (path.parent / target.split('#')[0]).resolve()
                    self.assertTrue(linked.is_relative_to(skill))
                    self.assertTrue(linked.is_file())

    def test_invalid_category_and_reserved_id(self):
        self.change_entries(lambda entries: entries[0].update(diataxis='unknown'))
        with self.assertRaises(ValueError):
            render_views(self.root)
        self.change_entries(lambda entries: entries[0].update(diataxis='reference', id='index'))
        with self.assertRaises(ValueError):
            render_views(self.root)

    def test_no_partial_output_on_invalid_input(self):
        (self.root / 'sources.json').write_text('not-json')
        with self.assertRaises(ValueError):
            compile_views(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_unregistered_local_link_fails_before_write(self):
        (self.root / 'content/extra.md').write_text('# Not registered\n')
        path = self.root / 'content/boot.md'
        path.write_text(path.read_text() + '\n[extra](extra.md)\n')
        with self.assertRaises(ValueError):
            compile_views(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_concurrent_source_edit_detected(self):
        from bsp_kb import compiler
        original_build = compiler.build

        def editing_build(root):
            path = root / 'content/boot.md'
            path.write_text(path.read_text() + '\nConcurrent edit.\n')
            return original_build(root)

        with patch.object(compiler, 'build', side_effect=editing_build):
            with self.assertRaisesRegex(ValueError, 'changed during compilation'):
                compile_views(self.root, self.output)
        self.assertFalse(self.output.exists())


if __name__ == '__main__':
    unittest.main()
