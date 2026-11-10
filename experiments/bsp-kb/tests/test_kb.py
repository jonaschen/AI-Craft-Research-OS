import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from bsp_kb.__main__ import ROOT, build, evaluate, search, validate


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ('content', 'evaluation'):
            shutil.copytree(ROOT / name, self.root / name)
        for name in ('sources.json', 'entries.json'):
            shutil.copy(ROOT / name, self.root / name)

    def change(self, name, fn):
        p = self.root / name
        data = json.loads(p.read_text())
        fn(data)
        p.write_text(json.dumps(data))

    def test_deterministic(self):
        self.assertEqual(build(self.root), build(self.root))
        self.assertEqual(search(build(self.root), 'DTB'), search(build(self.root), 'DTB'))

    def test_missing_field(self):
        self.change('entries.json', lambda d: d[0].pop('version'))
        with self.assertRaises(ValueError): validate(self.root)

    def test_duplicate(self):
        self.change('entries.json', lambda d: d.append(copy.deepcopy(d[0])))
        with self.assertRaises(ValueError): validate(self.root)

    def test_unknown_source(self):
        self.change('entries.json', lambda d: d[0].update(sources=['unknown']))
        with self.assertRaises(ValueError): validate(self.root)

    def test_digest(self):
        self.change('sources.json', lambda d: d[0].update(sha256='invalid'))
        with self.assertRaises(ValueError): validate(self.root)

    def test_broken_link(self):
        p = self.root / 'content/bsp.md'
        p.write_text(p.read_text() + '\n[missing](missing.md)\n')
        with self.assertRaises(ValueError): validate(self.root)

    def test_path_escape(self):
        self.change('entries.json', lambda d: d[0].update(path='../sources.json'))
        with self.assertRaises(ValueError): validate(self.root)

    def test_empty_and_unknown(self):
        for q in ('', '   ', 'zzzznonexistent'):
            self.assertEqual([], search(build(self.root), q))

    def test_languages_and_filter(self):
        chunks = build(self.root)
        for q in ('驅動', 'probe'):
            result = search(chunks, q, topic='drivers')
            self.assertTrue(result)
            self.assertTrue(all(c['topic'] == 'drivers' for c in result))
        self.assertEqual([], search(chunks, 'probe', topic='nonexistent'))

    def test_deletion(self):
        self.change('entries.json', lambda d: d.pop(0))
        self.assertNotIn('bsp', {c['entry_id'] for c in build(self.root)})

    def test_citation_integrity(self):
        for c in build(self.root):
            self.assertTrue(c['sources'])
            self.assertTrue((self.root / c['path']).is_file())
            self.assertTrue(all(s['sha256'] and s['version'] for s in c['sources']))

    def test_answer_isolation(self):
        before = build(self.root)
        (self.root / 'evaluation/secret.md').write_text('DO_NOT_EXPORT_ORACLE')
        self.assertEqual(before, build(self.root))
        self.assertNotIn('DO_NOT_EXPORT_ORACLE', json.dumps(build(self.root)))

    def test_benchmark(self):
        self.assertTrue(evaluate(self.root, build(self.root))['passed'])

    def test_cli_json_and_errors(self):
        p = subprocess.run([sys.executable, '-m', 'bsp_kb', 'search', 'DTB', '--json'],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        self.assertTrue(json.loads(p.stdout))
        p = subprocess.run([sys.executable, '-m', 'bsp_kb', 'search', 'DTB', '--limit', '0'],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)

    def test_export_jsonl(self):
        p = subprocess.run([sys.executable, '-m', 'bsp_kb', 'export'], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        rows = [json.loads(line) for line in p.stdout.splitlines()]
        self.assertEqual(rows, build(ROOT))


if __name__ == '__main__':
    unittest.main()
