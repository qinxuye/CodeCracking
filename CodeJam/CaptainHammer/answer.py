from __future__ import division
from math import asin, pi

g = 9.8

def main(input, output):
    with open(input) as input_f:
        with open(output, 'w') as output_f:
            n_cases = int(input_f.readline().strip())

            for case_num in range(1, n_cases+1):
                print 'solving case ', case_num

                v, d = input_f.readline().strip().split()
                v, d = float(v), float(d)

                tmp = g * d / (v ** 2)
                if tmp > 1.0:
                    tmp = 1.0
                theta = 90 * asin(tmp) / pi
                
                output_f.write('Case #%d: %.7f' % (
                    case_num, theta
                ))
                if n_cases != case_num:
                    output_f.write('\n')

if __name__ == "__main__":
    input = 'test.txt'
    output = input.rsplit('.', 1)[0] + '.out'

    import time

    start = time.time()
    main(input, output)
    end = time.time()

    print 'spend %s sec' % (end - start)