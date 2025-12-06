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

fresh = set()
for i in ingr:
    for (a, b) in ranges:
        if i >= a and i <= b:
            fresh.add(i)
print(f"Solution part 1: {len(fresh)}")