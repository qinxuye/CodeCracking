def main(input, output):
    with open(input) as input_f:
        with open(output, 'w') as output_f:
            n_cases = int(input_f.readline().strip())

            for case_num in range(1, n_cases+1):
                print 'solving case ', case_num

                n_lines = int(input_f.readline().strip())
                cards = [input_f.readline() for _ in range(n_lines)]
                
                costs = 0
                for i in range(1, n_lines):
                    if cards[i] < cards[i-1]:
                        costs += 1
                    cards = sorted(cards[:i+1]) + cards[i+1:]
                
                output_f.write('Case #%d: %d' % (
                    case_num, costs
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