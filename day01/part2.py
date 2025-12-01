import math


dial = 50
code = 0

with open("day01/input.txt") as f:
    for l in f.readlines():
        if l.startswith('L'):
            delta = int(l[1:])
            for i in range(delta):
                dial -= 1
                if dial == 0:
                    code += 1
                elif dial == -1:
                    dial = 99
        else:
            delta = int(l[1:])
            for i in range(delta):
                dial += 1
                if dial == 100:
                    code += 1
                    dial = 0
        
        print(code, dial)
print(f"Solution part 2: {code}")