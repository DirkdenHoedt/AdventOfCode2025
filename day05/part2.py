ranges = []
ingr = []

with open("day05/input.txt") as f:
    raw = f.read()
    ranges_, ingr_ = raw.split('\n\n')
    
    for r in ranges_.split('\n'):
        a, b = r.strip().split('-')
        ranges.append((int(a), int(b)))
    
    for i in ingr_.split('\n'):
        ingr.append(int(i))

ranges = sorted(ranges)

fresh_ranges = []
for (a, b) in ranges:
    out_range = True
    for i, (x, y) in enumerate(fresh_ranges):
        if a >= x and b <= y:
            out_range = False
        elif a >= x and a <= y:
            fresh_ranges[i] = (x, b)
            out_range = False
        elif b >= x and b <= y:
            fresh_ranges[i] = (a, y)
            out_range = False
    if out_range:
        fresh_ranges.append((a, b))

# print(fresh_ranges)
print(f"Solution part 2: {sum(map(lambda x: x[1] - x[0] + 1, fresh_ranges))}")