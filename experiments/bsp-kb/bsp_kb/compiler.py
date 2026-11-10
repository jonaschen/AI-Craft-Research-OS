"""Deterministic human/agent views of the registered, public BSP corpus."""

import hashlib
import json
import os
import posixpath
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote

from .__main__ import build, inside, validate

CATEGORIES = ('tutorials', 'how-to', 'reference', 'explanation')
TEMPLATE = 'templates/bsp-knowledge/SKILL.md'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()


def _input_paths(root, entries):
    paths = {name: inside(root, name) for name in ('entries.json', 'sources.json', TEMPLATE)}
    for entry in entries:
        name = 'content/' + entry['path']
        paths[name] = inside(root / 'content', entry['path'])
    # Bind both renderer and chunking implementation, without host-specific paths.
    for name in ('compiler.py', '__main__.py'):
        paths['@implementation/' + name] = Path(__file__).with_name(name)
    return paths


def _fingerprints(paths):
    return {name: digest(path.read_bytes()) for name, path in sorted(paths.items())}


def _rewrite_links(text, source, destination, mapping):
    def replace(match):
        target = match.group(2)
        if target.startswith(('https://', 'http://', '#')):
            return match.group(0)
        name, sep, anchor = target.partition('#')
        resolved = (source.parent / unquote(name)).resolve()
        if resolved not in mapping:
            raise ValueError(f'local link is not a registered content entry: {target}')
        relative = posixpath.relpath(mapping[resolved], posixpath.dirname(destination))
        return f'[{match.group(1)}]({relative}{sep}{anchor})'
    return re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace, text)


def render_views(root):
    """Return a path->bytes map; read only registered content, never evaluation."""
    root = Path(root).resolve()
    # Detect edits during rendering, including changes to the registration files.
    initial = {name: inside(root, name).read_bytes() for name in ('entries.json', 'sources.json')}
    entries, sources = validate(root)
    entries = sorted(entries, key=lambda entry: entry['id'])
    paths = _input_paths(root, entries)
    before = _fingerprints(paths)
    if any(digest(data) != before[name] for name, data in initial.items()):
        raise ValueError('corpus changed during compilation; retry with a stable corpus')
    human_paths, skill_paths = {}, {}
    for entry in entries:
        if entry['id'] == 'index':
            raise ValueError('entry ID index is reserved for generated navigation')
        category = entry.get('diataxis', 'explanation')
        if category not in CATEGORIES:
            raise ValueError(f'invalid diataxis category: {category}')
        source = paths['content/' + entry['path']]
        if source in human_paths:
            raise ValueError('multiple entries reference the same content file')
        human_paths[source] = f"human/{category}/{entry['id']}.md"
        skill_paths[source] = f"skills/bsp-knowledge/references/{entry['id']}.md"

    files = {}
    groups = {category: [] for category in CATEGORIES}
    skill_index = ['# 教材索引', '', '依問題只讀需要的教材；版本與來源記錄見各文件。', '']
    llms = ['# BSP knowledge bundle', '', '> Generated from registered public lessons. Expert review pending.', '', '## Lessons', '']
    for entry in entries:
        source = paths['content/' + entry['path']]
        category = entry.get('diataxis', 'explanation')
        metadata = {key: entry[key] for key in ('id', 'title', 'topic', 'version', 'status', 'sources', 'reviewed', 'license')}
        metadata.update(diataxis=category, canonical_path='content/' + entry['path'],
                        content_sha256=before['content/' + entry['path']])
        # JSON values are valid YAML scalars/flow sequences; no YAML dependency.
        header = '---\n' + ''.join(f'{key}: {json.dumps(value, ensure_ascii=False)}\n'
                                  for key, value in metadata.items()) + '---\n\n'
        text = source.read_text(encoding='utf-8')
        for mapping in (human_paths, skill_paths):
            destination = mapping[source]
            files[destination] = (header + _rewrite_links(text, source, destination, mapping)).encode()
        groups[category].append(f"- [{entry['title']}]({entry['id']}.md) — {entry['version']}")
        skill_index.append(f"- [{entry['title']}]({entry['id']}.md) — {entry['version']}; {entry['status']}")
        llms.append(f"- [{entry['title']}]({human_paths[source]}): {entry['version']}")
    for category, links in groups.items():
        body = '\n'.join(links) if links else '尚無已登錄教材；此分類待補。'
        files[f'human/{category}/index.md'] = f'# {category}\n\n{body}\n'.encode()
    files['human/index.md'] = ('# BSP 知識導覽\n\n由同一份來源編譯。請回到原始教材修改後重新編譯。\n\n' +
                               '\n'.join(f'- [{c}]({c}/index.md)' for c in CATEGORIES) + '\n').encode()
    files['llms.txt'] = ('\n'.join(llms) + '\n').encode()
    files['skills/bsp-knowledge/references/index.md'] = ('\n'.join(skill_index) + '\n').encode()
    files['skills/bsp-knowledge/references/sources.json'] = encode(list(sources.values()))
    files['skills/bsp-knowledge/SKILL.md'] = paths[TEMPLATE].read_bytes()
    chunks = build(root)
    # Export paths point into the bundle, not into the original checkout.
    for chunk in chunks:
        source = inside(root, chunk['path'])
        chunk['canonical_path'] = chunk['path']
        chunk['path'] = human_paths[source]
        chunk['text'] = _rewrite_links(chunk['text'], source, chunk['path'], human_paths)
        chunk['content_sha256'] = before[chunk['canonical_path']]
    files['agent/index.json'] = encode({'schema_version': 1, 'chunks': chunks})
    files['agent/context.jsonl'] = ''.join(json.dumps(chunk, ensure_ascii=False, sort_keys=True) + '\n'
                                           for chunk in chunks).encode()
    if before != _fingerprints(paths):
        raise ValueError('corpus changed during compilation; retry with a stable corpus')
    output_hashes = {name: digest(data) for name, data in sorted(files.items())}
    manifest = {'schema_version': 1, 'bundle_format': 'bsp-knowledge', 'bundle_version': 1, 'inputs': before, 'outputs': output_hashes,
                'revision': digest(encode(before)), 'bundle_sha256': digest(encode(output_hashes)),
                'entry_count': len(entries), 'chunk_count': len(chunks),
                'scope': 'Registered public corpus only; no evaluation answers or upstream full text.',
                'limitations': 'Hashes detect drift, not authenticity, factual correctness or hardware qualification.'}
    files['manifest.json'] = encode(manifest)
    return files


def _output_path(root, output):
    root, output = Path(root).resolve(), Path(output).absolute()
    if output.is_symlink():
        raise ValueError('output must not be a symbolic link')
    output = output.resolve()
    if root.is_relative_to(output):
        raise ValueError('output must not be the corpus or an ancestor')
    for directory in ('content', 'evaluation', 'templates', 'bsp_kb', 'tests'):
        if output.is_relative_to(root / directory):
            raise ValueError('output must not be inside a source directory')
    return output


def compile_views(root, output):
    """Compile into a NEW directory. Refuse existing paths; never remove user files."""
    output = _output_path(root, output)
    if output.exists():
        raise ValueError('output already exists; choose a new output directory')
    files = render_views(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.bsp-build-', dir=output.parent))
    try:
        for name, data in sorted(files.items()):
            path = staging / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        # mkdir is exclusive: a concurrent writer must never be overwritten.
        output.mkdir()
        # A partial bundle after an I/O failure is detectable by check_views.
        for child in staging.iterdir():
            os.rename(child, output / child.name)
    finally:
        shutil.rmtree(staging)
    manifest = json.loads(files['manifest.json'])
    return {'compiled': True, 'output': str(output), 'files': len(files),
            'revision': manifest['revision'], 'bundle_sha256': manifest['bundle_sha256'],
            'entries': manifest['entry_count'], 'chunks': manifest['chunk_count']}


def check_views(root, output):
    """Compare the entire bundle with a fresh render; ignore untrusted manifest paths."""
    output = _output_path(root, output)
    expected = render_views(root)
    actual = {}
    invalid = []
    if output.exists() and not output.is_dir():
        raise ValueError('output is not a directory')
    if output.exists():
        for parent, dirs, names in os.walk(output, followlinks=False):
            for name in list(dirs):
                path = Path(parent) / name
                if path.is_symlink():
                    invalid.append(path.relative_to(output).as_posix())
                    dirs.remove(name)
            for name in names:
                path = Path(parent) / name
                relative = path.relative_to(output).as_posix()
                if path.is_symlink() or not path.is_file():
                    invalid.append(relative)
                else:
                    actual[relative] = digest(path.read_bytes())
    missing = sorted(set(expected) - set(actual))
    unexpected = sorted(set(actual) - set(expected))
    changed = sorted(name for name in set(actual) & set(expected) if actual[name] != digest(expected[name]))
    return {'valid': not (missing or unexpected or changed or invalid),
            'missing': missing, 'unexpected': unexpected, 'changed': changed,
            'invalid_paths': sorted(invalid), 'files': len(expected)}
