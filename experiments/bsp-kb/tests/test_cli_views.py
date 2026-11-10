"""CLI contract tests for compilation and drift checking."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ViewCLITests(unittest.TestCase):
    def test_compile_check_and_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'views'
            def run(command):
                return subprocess.run([sys.executable, '-m', 'bsp_kb', command, '--output', str(output)], capture_output=True, text=True)
            built = run('compile')
            self.assertEqual(built.returncode, 0, built.stderr)
            self.assertTrue(json.loads(built.stdout)['compiled'])
            checked = run('check')
            self.assertEqual(checked.returncode, 0, checked.stderr)
            self.assertTrue(json.loads(checked.stdout)['valid'])
            (output / 'llms.txt').write_text('tampered')
            changed = run('check')
            self.assertEqual(changed.returncode, 1)
            self.assertIn('llms.txt', json.loads(changed.stdout)['changed'])
            refused = run('compile')
            self.assertEqual(refused.returncode, 2)
            self.assertEqual((output / 'llms.txt').read_text(), 'tampered')
