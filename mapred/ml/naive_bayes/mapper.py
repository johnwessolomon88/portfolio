import sys
import argparse
import nltk

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--stopwords', type=str, default='')
    return p.parse_args()

if __name__ == '__main__':
    # postive label = 1
    # negative label = 0
    
    # dta_on_ft
    # ---------
    # key = feature
    # val = tuple(negative count, positive count)
    dta_on_ft = {}
    args = get_args()
    stop = set(args.stopwords.split('|'))
    tokenizer = nltk.tokenize.TreebankWordTokenizer()
    for l in sys.stdin:
        txt, lbl = l.strip().split('\t')
        lbl = int(lbl)
        tkns = set(tokenizer.tokenize(txt))
        for tkn in tkns:
            if tkn in stop:
                continue
            dta = dta_on_ft.get(tkn, [0, 0])
            dta[lbl] += 1
            dta_on_ft[tkn] = dta

    for ft, dta in dta_on_ft.iteritems():
        print str(ft) + '\t' + str(dta[0]) + '\t' + str(dta[1])
