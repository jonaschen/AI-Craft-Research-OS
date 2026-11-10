import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def tokens(text):
    parts = re.findall(r'[a-z0-9_]+|[\u3400-\u9fff]+', text.lower())
    return [t for p in parts for t in ([p] if p.isascii() or len(p) == 1 else
                                      [p[i:i+2] for i in range(len(p)-1)])]


def inside(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'path outside corpus: {name}')
    return path


def validate(root):
    sources = read(root / 'sources.json')
    entries = read(root / 'entries.json')
    ids = set()
    for s in sources:
        for key in ('id', 'url', 'version', 'retrieved', 'sha256', 'scope', 'license',
                    'reuse_basis', 'author', 'permissions'):
            if not s.get(key):
                raise ValueError(f'source missing {key}')
        if s['id'] in ids or not s['url'].startswith('https://'):
            raise ValueError('duplicate source or invalid URL')
        if not re.fullmatch('[0-9a-f]{64}', s['sha256']):
            raise ValueError('invalid source digest')
        date.fromisoformat(s['retrieved'])
        ids.add(s['id'])
    seen = set()
    for e in entries:
        for key in ('id', 'title', 'topic', 'version', 'sources', 'reviewed', 'status', 'path', 'license'):
            if not e.get(key):
                raise ValueError(f'entry missing {key}')
        if e['id'] in seen or not re.fullmatch('[a-z0-9-]+', e['id']):
            raise ValueError('duplicate or invalid entry ID')
        seen.add(e['id'])
        date.fromisoformat(e['reviewed'])
        if not isinstance(e['sources'], list) or not set(e['sources']) <= ids:
            raise ValueError('unknown source')
        path = inside(root / 'content', e['path'])
        text = path.read_text(encoding='utf-8')
        if not text.startswith('# ') or '## ' not in text:
            raise ValueError('missing document sections')
        headings = re.findall(r'^## (.+)$', text, re.M)
        if len(set(headings)) != len(headings):
            raise ValueError('duplicate section heading')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if not target.startswith(('https://', 'http://', '#')):
                if not inside(root, str(path.parent.relative_to(root) / target.split('#')[0])).is_file():
                    raise ValueError(f'broken local link: {target}')
    if not entries or not sources:
        raise ValueError('empty corpus')
    return entries, {s['id']: s for s in sources}


def build(root):
    entries, sources = validate(root)
    chunks = []
    for e in entries:
        text = inside(root / 'content', e['path']).read_text(encoding='utf-8')
        sections = re.split(r'^## (.+)\n', text, flags=re.M)
        for heading, body in zip(sections[1::2], sections[2::2]):
            sid = hashlib.sha256(heading.encode()).hexdigest()[:12]
            chunks.append({'id': e['id'] + ':' + sid, 'entry_id': e['id'],
                           'title': e['title'], 'heading': heading, 'text': body.strip(),
                           'topic': e['topic'], 'version': e['version'], 'status': e['status'],
                           'path': 'content/' + e['path'],
                           'sources': [sources[s] for s in e['sources']]})
    return sorted(chunks, key=lambda c: c['id'])


def search(chunks, query, limit=3, topic=None):
    q = set(tokens(query))
    if not q:
        return []
    counts = [Counter(tokens(c['title'] + ' ' + c['heading'] + ' ' + c['text'])) for c in chunks]
    df = Counter(t for count in counts for t in count)
    results = []
    for c, count in zip(chunks, counts):
        if topic and c['topic'] != topic:
            continue
        score = sum((1 + math.log(count[t])) * math.log(1 + len(chunks) / df[t])
                    for t in q if count[t]) / math.sqrt(max(1, sum(count.values())))
        if score > 0:
            results.append(dict(c, score=round(score, 6)))
    return sorted(results, key=lambda c: (-c['score'], c['id']))[:limit]


def evaluate(root, chunks):
    cases = read(root / 'evaluation' / 'cases.json')
    results = []
    for c in cases:
        found = search(chunks, c['query'])
        got = sorted({r['entry_id'] for r in found})
        passed = bool(set(c['expected']) & set(got)) if c['expected'] else not got
        results.append(dict(c, retrieved=got, passed=passed))
    scoped = [r for r in results if r['expected']]
    recall = sum(r['passed'] for r in scoped) / len(scoped)
    return {'recall_at_3': recall, 'passed': recall >= .8 and all(r['passed'] for r in results if not r['expected']),
            'cases': results, 'limitations': 'Author-created development set; not independent expert or agent accuracy evaluation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('validate', 'build', 'export', 'evaluate'):
        sub.add_parser(name)
    p = sub.add_parser('search')
    p.add_argument('query')
    p.add_argument('--topic')
    p.add_argument('--limit', type=int, default=3)
    p.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        chunks = build(args.root)
        if args.command == 'validate':
            result = {'valid': True, 'chunks': len(chunks)}
        elif args.command == 'build':
            result = {'schema_version': 1, 'chunks': chunks}
        elif args.command == 'export':
            for c in chunks:
                print(json.dumps(c, ensure_ascii=False, sort_keys=True))
            return 0
        elif args.command == 'evaluate':
            result = evaluate(args.root, chunks)
        else:
            if args.limit < 1:
                raise ValueError('--limit must be positive')
            result = search(chunks, args.query, args.limit, args.topic)
            if not args.json:
                for r in result:
                    print(f"{r['id']} {r['title']} / {r['heading']} [{r['score']}]\n{r['text']}\n")
                return 0
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 1 if args.command == 'evaluate' and not result['passed'] else 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
