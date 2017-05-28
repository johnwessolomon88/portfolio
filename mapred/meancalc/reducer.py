import sys

if __name__ == '__main__':
    cur_uid = None
    cur_val = None
    cur_tot = 0
    for l in sys.stdin:
        uid, val, tot = l.strip().split('\t')
        val = float(val)
        tot = float(tot)
        if uid == cur_uid:
            cur_val += val
            cur_tot += tot
        else:
            if cur_uid:
                avg = cur_val / float(cur_tot)
                print str(cur_uid) + '\t' + str(avg)
            cur_uid = uid
            cur_val = val
            cur_tot = tot
    if cur_uid == uid:
        avg = cur_val / float(cur_tot)
        print str(cur_uid) + '\t' + str(avg)

