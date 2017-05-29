import sys

if __name__ == '__main__':
    last_ft = None
    cur_neg = 0
    cur_pos = 0
    for l in sys.stdin:
        ft, neg, pos = l.strip().split('\t')
        if last_ft == ft:
            cur_neg += int(neg)
            cur_pos += int(pos)
        elif last_ft is not None:
            print str(last_ft) + '\t' + str(cur_neg) + '\t' + str(cur_pos)
        last_ft = ft
        cur_neg = int(neg)
        cur_pos = int(pos)
    print str(last_ft) + '\t' + str(cur_neg) + '\t' + str(cur_pos)
        
