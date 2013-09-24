from collections import defaultdict

DEBUG = False

UNDEFINED, CONFIRM, CONFLICT = range(3)

def main(input, output):
    with open(input) as input_f:
        with open(output, 'w') as output_f:
            n_cases = int(input_f.readline().strip())

            for case_num in range(1, n_cases+1):
                print 'solving case ', case_num
                # each case
                result = True
                
                n_lines = int(input_f.readline().strip())
                pairs = [tuple(input_f.readline().strip().split()) for _ in range(n_lines)]

                paired_maps = defaultdict(set)
                for pair in pairs:
                    paired_maps[pair[0]].add(pair[1])
                    paired_maps[pair[1]].add(pair[0])
                
                name_to_groups = {}
                tracebacks = []
                cursor = 0
                while True:
                    pair = pairs[cursor]
                    states = [UNDEFINED, UNDEFINED]
                    groups = [0, 0]
                    
                    for name in pair:
                        idx = pair.index(name)
                        other_idx = 1 if idx == 0 else 0
                        other = pair[other_idx]

                        for d_name in paired_maps[name]:
                            if d_name in name_to_groups:
                                tmp_group = -name_to_groups[d_name]
                                if groups[idx] == 0:
                                    groups[idx] = tmp_group
                                elif groups[idx] != tmp_group:
                                    states[idx] = CONFLICT
                                    groups[idx] = 0
                                    break
                        if groups[idx] != 0:
                            states[idx] = CONFIRM

                    if states[0] == CONFLICT or states[1] == CONFLICT or \
                       (states[0] == CONFIRM and states[1] == CONFIRM and groups[0] == groups[1]):
                        if len(tracebacks) == 0:
                            result = False
                            break
                        cursor, name_to_groups = tracebacks.pop()
                        if DEBUG: 
                            print 'trace back to ', cursor, ', case: ', case_num
                            print 'cursors: [', ', '.join([str(t[0]) for t in tracebacks]), ']'
                        pair = pairs[cursor]
                        name_to_groups[pair[0]] = 1
                        name_to_groups[pair[1]] = -1
                    elif states[0] == CONFIRM or states[1] == CONFIRM:
                        if states[1] == UNDEFINED:
                            groups[1] = -groups[0]
                        elif states[0] == UNDEFINED:
                            groups[0] = -groups[1]
                        name_to_groups[pair[0]] = groups[0]
                        name_to_groups[pair[1]] = groups[1]
                    else:
                        # Check
                        assert states[0] == UNDEFINED
                        assert states[1] == UNDEFINED

                        name_to_groups[pair[0]] = -1
                        name_to_groups[pair[1]] = 1
                        tracebacks.append((cursor, name_to_groups.copy()))

                    cursor += 1
                    if cursor >= len(pairs):
                        break

                output_f.write('Case #%d: %s' % (
                    case_num, 'Yes' if result is True else 'No'
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