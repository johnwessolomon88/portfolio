import sys

if __name__ == '__main__':
    # dta_on_uid
    # ----------
    # key = uid
    # val = tuple(value sum, number of observations)
    dta_on_uid = {}
    for l in sys.stdin:
        uid, val = l.strip().split('\t')
        uid = uid
        val = float(val)
        dta = dta_on_uid.get(uid, [0, 0])
        dta[0] += val
        dta[1] += 1
        dta_on_uid[uid] = dta
    for uid, dta in dta_on_uid.iteritems():
        print str(uid) + '\t' + str(dta[0]) + '\t' + str(dta[1])


