import unittest
import subprocess

class TestReducer(unittest.TestCase):
    def test_run(self):
        cmd = '''
        echo "a\t1\nb\t2\nc\t3\na\t2" |
        python mapred/meancalc/mapper.py |
        sort -k1,1 |
        python mapred/meancalc/reducer.py
        '''
        expected = [
            ['a', '1.5'],
            ['b', '2.0'],
            ['c', '3.0'],
        ]
        out = subprocess.check_output(cmd, shell=True).strip()
        rows = [r.split('\t') for r in out.split('\n')]
        for i in range(len(rows)):
            self.assertEqual(rows[i], expected[i])

if __name__ == '__main__':
    unittest.main()
