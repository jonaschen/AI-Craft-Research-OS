"""Stateless observations from untrusted UART text; never execute log contents."""
import hashlib
import re

MAX_BYTES = 1024 * 1024
BASE = 'https://raw.githubusercontent.com/torvalds/linux/v6.12/'
# Signature recognition, not root-cause inference. Rules are intentionally narrow.
RULES = (
    ('rootfs-mount', r'VFS: Unable to mount root fs', 'root-filesystem',
     '觀察到根檔案系統掛載失敗訊息。',
     ['核對 root= 與實際映像／分割區。', '核對儲存控制器與檔案系統支援及前序日誌。'],
     'init/do_mounts.c'),
    ('init-missing', r'No working init found\.', 'userspace-init',
     '觀察到核心找不到可執行 init 的訊息。',
     ['核對 rootfs 中 init 的路徑、架構與直譯器。', '保存核心版本與完整前序錯誤，不直接重建或刷寫。'],
     'init/main.c'),
    ('kernel-panic', r'Kernel panic - not syncing:', 'kernel',
     '觀察到 kernel panic 標記；此標記不足以判定根因。',
     ['保存 panic 前的第一個錯誤及完整日誌。', '核對核心版本、組態與映像雜湊。'],
     'kernel/panic.c'),
)
# Only recognize explicit banners. No timestamp or absence-of-output inference.
STAGES = (
    ('bootloader', re.compile(r'^U-Boot \d{4}\.\d{2}')),
    ('kernel', re.compile(r'^(?:\[\s*\d+(?:\.\d+)?\]\s*)?Linux version \S+')),
)
ANSI = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')


def analyze_uart(text):
    if not isinstance(text, str):
        raise ValueError('UART input must be text')
    raw = text.encode('utf-8')
    if len(raw) > MAX_BYTES:
        raise ValueError('UART input exceeds 1 MiB')
    if '\x00' in text:
        raise ValueError('UART input contains NUL bytes; decode the capture first')
    events, stages = [], []
    for number, line in enumerate(text.splitlines(), 1):
        clean = ANSI.sub('', line)
        clean = ''.join(c for c in clean if c.isprintable() or c == '\t')
        for stage, pattern in STAGES:
            if pattern.search(clean):
                stages.append({'stage': stage, 'line': number})
        for id, pattern, area, observation, checks, source in RULES:
            match = re.search(pattern, clean)
            if match:
                events.append({'rule_id': id, 'line': number, 'signature': match.group(),
                               'area': area, 'observation': observation,
                               'next_checks': list(checks), 'source': BASE + source,
                               'certainty': 'signature-only'})
    return {'schema_version': 1, 'ruleset_version': '1',
            'input_sha256': hashlib.sha256(raw).hexdigest(), 'line_count': len(text.splitlines()),
            'status': 'signatures-found' if events else 'insufficient-evidence',
            'observed_stages': stages, 'events': events, 'root_cause': None,
            'limitations': ['Synthetic-fixture validated; not a hardware diagnosis.',
                            'Matching strings may be quoted or forged; verify capture provenance.',
                            'No matching signature does not imply successful boot.',
                            'Multiple boots are not separated; line numbers preserve input order.']}
