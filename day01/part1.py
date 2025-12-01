dial = 50
code = 0

with open("day01/input.txt") as f:
    for l in f.readlines():
        if l.startswith('L'):
            dial -= int(l[1:])
        else:
            dial += int(l[1:])
        dial %= 100
        if dial == 0:
            code += 1
print(f"Solution part 1: {code}")