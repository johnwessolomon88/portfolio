import unittest
import subprocess

class TestMapper(unittest.TestCase):
    def test_run(self):
        cmd = '''
        echo "a\t1\nb\t2\nc\t3\na\t2" | 
        python mapred/meancalc/mapper.py
        '''
        expected = [
            ['a', '3.0', '2'],
            ['b', '2.0', '1'],
            ['c', '3.0', '1'],
        ]
        out = subprocess.check_output(cmd, shell=True).strip()
        str_rows = out.split('\n')
        rows = [sr.split('\t') for sr in str_rows]
        rows.sort(key=lambda r:r[0])
        for i in range(len(rows)):
            self.assertEqual(rows[i], expected[i])

if __name__ == '__main__':
    unittest.main()
        
