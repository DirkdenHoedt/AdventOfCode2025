answer = 0
with open("day02/input.txt") as f:
    for nums in f.read().strip().split(','):
        a, b = nums.split('-')
        for i in range(int(a), int(b) + 1):
            num = str(i)
            if num[:len(num)//2] == num[len(num)//2:]:
                answer += i
print(answer)