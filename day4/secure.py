import itertools

def adjacent(passwd):
    passwd = str(passwd)
    i = 0
    while i < len(passwd):
        num = passwd[i]
        if i == len(passwd) - 1:
            return False
        next_num = passwd[i+1]
        if num == next_num:
            return True
        i += 1

def increase(passwd):
    passwd = str(passwd)
    i = 0
    while i < len(passwd):
        num = passwd[i]
        if i == len(passwd) -1: 
            return True
        next_num = passwd[i+1]
        if next_num < num:
            return False
        i += 1
 

    
possible = []
possible2 = []

for x in range(130254, 678276):
    if increase(x) and adjacent(x):
        possible.append(x)

print(f'Part 1 is {len(possible)}')

def part2(passwd):
    passwd = str(passwd)
    for x in passwd:
        count = passwd.count(x)
        if count == 2:
            return True

for x in range(130254, 678276):
    if increase(x) and part2(x):
        possible2.append(x)

print(f'Part 2 is {len(possible2)}')