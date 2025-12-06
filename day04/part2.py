import copy


rolls = []
locations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
answer = 0

with open("day04/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line):
            if c == '@':
                rolls.append((i, j))
rolls_found = True
while rolls_found:
    rolls_found = False
    old_rolls = copy.deepcopy(rolls)
    for (x, y) in old_rolls:
        roll_count = 0
        for (dx, dy) in locations:
            if (x + dx, y + dy) in old_rolls:
                roll_count += 1
        if roll_count < 4:
            answer += 1
            rolls_found = True
            rolls.remove((x, y))

print(f"Solution part 2: {answer}")