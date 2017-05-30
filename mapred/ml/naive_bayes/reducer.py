import sys

if __name__ == '__main__':
    dta_on_ft = {}
    for l in sys.stdin:
        ft, neg, pos = l.strip().split('\t')
        dta = dta_on_ft.get(ft, [0, 0])
        dta[0] += int(neg)
        dta[1] += int(pos)
        dta_on_ft[ft] = dta

    for ft,dta in dta_on_ft.iteritems():
        print str(ft) + '\t' + str(dta[0]) + '\t' + str(dta[1])
