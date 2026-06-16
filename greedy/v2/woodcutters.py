n = int(input())
if n <= 2:
    print(max(0, n))
    exit()

pairs = list(tuple(map(int, input().split())) for _ in range(n))

total = 2
maxX = pairs[0][0]
for i in range(1, n - 1):
    x, h = pairs[i]
    if x - h > maxX:
        total += 1
        maxX = x
    elif x + h < pairs[i + 1][0]:
        total += 1
        maxX = x + h
    else:
        maxX = x

print(total)