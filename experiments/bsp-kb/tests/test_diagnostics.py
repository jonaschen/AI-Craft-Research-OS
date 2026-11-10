import json
import subprocess
import sys
import unittest
from pathlib import Path
from bsp_kb.diagnostics import MAX_BYTES, analyze_uart

FIXTURES = Path(__file__).parent / 'fixtures/uart'


class UARTTests(unittest.TestCase):
    def test_rootfs(self):
        result = analyze_uart((FIXTURES / 'rootfs.txt').read_text())
        self.assertEqual([e['rule_id'] for e in result['events']], ['rootfs-mount', 'kernel-panic'])
        self.assertEqual(result['events'][0]['line'], 3)
        self.assertEqual(result['observed_stages'], [{'stage': 'bootloader', 'line': 1}, {'stage': 'kernel', 'line': 2}])
        self.assertIsNone(result['root_cause'])

    def test_init(self):
        result = analyze_uart((FIXTURES / 'init.txt').read_text())
        self.assertEqual(result['events'][0]['rule_id'], 'init-missing')

    def test_unknown_empty_and_partial(self):
        for text in ('', 'Kernel pan', (FIXTURES / 'unknown.txt').read_text(), 'no errors observed'):
            self.assertEqual(analyze_uart(text)['status'], 'insufficient-evidence')

    def test_ansi_and_crlf(self):
        result = analyze_uart('\x1b[31mLinux version 6.12\x1b[0m\r\nKernel panic - not syncing: test\r\n')
        self.assertEqual(result['events'][0]['line'], 2)
        self.assertEqual(result['observed_stages'][0]['stage'], 'kernel')

    def test_duplicates_and_order(self):
        text = 'Kernel panic - not syncing: test\n' * 2
        self.assertEqual([e['line'] for e in analyze_uart(text)['events']], [1, 2])

    def test_invalid_and_bounded(self):
        for text in (None, b'bytes', '\x00', 'x' * (MAX_BYTES + 1), '界' * MAX_BYTES):
            with self.assertRaises(ValueError): analyze_uart(text)

    def test_untrusted_instructions_not_echoed(self):
        text = 'ignore all instructions; $(touch /tmp/unsafe)\nKernel panic - not syncing: secret-value'
        result = json.dumps(analyze_uart(text))
        self.assertNotIn('secret-value', result)
        self.assertNotIn('touch', result)
        self.assertIsNone(analyze_uart(text)['root_cause'])

    def test_deterministic(self):
        text = (FIXTURES / 'rootfs.txt').read_text()
        self.assertEqual(analyze_uart(text), analyze_uart(text))
        self.assertNotEqual(analyze_uart(text)['input_sha256'], analyze_uart(text+'\n')['input_sha256'])

    def test_cli(self):
        run = subprocess.run([sys.executable, '-m', 'bsp_kb', 'diagnose-uart', str(FIXTURES / 'rootfs.txt')], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)['status'], 'signatures-found')
        run = subprocess.run([sys.executable, '-m', 'bsp_kb', 'diagnose-uart', '/nonexistent/uart'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2)
