rolls = []
locations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
answer = 0

with open("day04/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, c in enumerate(line):
            if c == '@':
                rolls.append((i, j))

for (x, y) in rolls:
    roll_count = 0
    for (dx, dy) in locations:
        if (x + dx, y + dy) in rolls:
            roll_count += 1
    if roll_count < 4:
        answer += 1

print(f"Solution part 1: {answer}")