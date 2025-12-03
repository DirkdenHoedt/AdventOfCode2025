batteries:list[list[int]] = []
answer = 0

with open("day03/input.txt") as f:
    for line in f.readlines():
        batteries.append(list(map(lambda x: int(x), list(line.strip()))))

for bank in batteries:
    nums = []
    index = 0
    for c in range(11, 0, -1):
        a = max(bank[index:-c])
        index = bank[index:-c].index(a) + 1 + index
        nums.append(str(a))
    nums.append(str(max(bank[index:])))
    answer += int(''.join(nums))
    print(int(''.join(nums)))
print(f"Solution for day 3: {answer}")