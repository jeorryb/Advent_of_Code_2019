import math

def parse_input(input):
    with open(input) as fh:
        lines = fh.readlines()
        return lines

def calc_fuel(mass):
    return math.floor(int(mass) / 3) - 2

lines = parse_input('/Users/jeorryb/Dropbox/AdventofCode_2019/day1/input.txt')

part_1 = sum([calc_fuel(x) for x in lines])

print(f'Part 1 is {part_1}')

def p2_calc(mass2):
    fuel_req = []
    while mass2 > 0:
        m = calc_fuel(mass2)
        if m > 0:
            fuel_req.append(m)
        mass2 = m
    return sum(fuel_req)

part_2 = sum([p2_calc(int(x)) for x in lines])

print(f'Part 2 is {part_2}')  