import itertools

def parse_input(input):
    with open(input) as fh:
        program = [int(x) for x in fh.readline().strip().split(',')]
        return program

program = parse_input('/Users/jeorryb/Dropbox/AdventofCode_2019/day2/input.txt')
program2 = parse_input('/Users/jeorryb/Dropbox/AdventofCode_2019/day2/input.txt')
program[1] = 12
program[2] = 2

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

for x in grouper(program, 4):
    if x[0] == 1:
        program[x[3]] = program[x[1]] + program[x[2]]
    elif x[0] == 2:
        program[x[3]] = program[x[1]] * program[x[2]]
    elif x[0] == 99:
        break

print(f'Part 1 is {program[0]}')

for i in range(100):
    for j in range(100):
        memory = program2.copy()
        memory[1], memory[2] = i, j
        for x in grouper(memory, 4):
            if x[0] == 1:
                memory[x[3]] = memory[x[1]] + memory[x[2]]
            elif x[0] == 2:
                memory[x[3]] = memory[x[1]] * memory[x[2]]
            elif x[0] == 99:
                break
        if memory[0] == 19690720:
            part2 = 100 * i + j
            print(f'Part 2 is {part2}')


