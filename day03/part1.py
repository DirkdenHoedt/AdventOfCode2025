batteries:list[list[int]] = []
answer = 0

with open("day03/input.txt") as f:
    for line in f.readlines():
        batteries.append(list(map(lambda x: int(x), list(line.strip()))))

for bank in batteries:
    a = max(bank)
    i = bank.index(a)
    if len(bank) == i+1:
        a = max(bank[:-1])
        i = bank.index(a)
    b = max(bank[i+1:])
    answer += a*10+b
print(f"Solution for day 3: {answer}")