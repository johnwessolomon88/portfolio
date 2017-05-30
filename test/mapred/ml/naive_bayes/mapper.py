import unittest
import subprocess

class TestMapper(unittest.TestCase):
    def test_run(self):
        docs = [
            'i like new things',
            'i dislike new things',
            'i hate old stuff',
        ]
        lbls = [1, 0, 0]
        cmd = 'echo "'
        for i in range(len(docs)):
            cmd += docs[i] + '\t' + str(lbls[i]) + '\n'
        cmd = cmd.strip()
        cmd += '" | python mapred/ml/naive_bayes/mapper.py'
        out = subprocess.check_output(cmd, shell=True).strip()
        exp_on_ft = {
            'i':[2,1], 'like':[0,1], 'new':[1,1], 'things':[1,1],
            'dislike':[1,0], 'hate':[1,0], 'old':[1,0], 'stuff':[1,0]
        }
        for l in out.split('\n'):
            ft, neg, pos = l.strip().split('\t')
            exneg, expos = exp_on_ft[ft]
            self.assertEqual(exneg, int(neg))
            self.assertEqual(expos, int(pos))

if __name__ == '__main__':
    unittest.main()
