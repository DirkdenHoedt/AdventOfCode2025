import textwrap

from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

answer = 0
with open("day02/input.txt") as f:
    for nums in f.read().strip().split(','):
        a, b = nums.split('-')
        for i in range(int(a), int(b) + 1):
            num = str(i)
            for x in range(1, len(num)):
                if all_equal(textwrap.wrap(num, x)):
                    answer += i
                    break

print(answer)