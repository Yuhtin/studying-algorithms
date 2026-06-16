n = int(input())
if n == 1:
    print(1)
    exit()

pairs = [tuple(map(int, input().split())) for _ in range(n)]

count = 2
last = pairs[0][0]

for i in range(1, n - 1):
    x, h = pairs[i]
    
    if x - h > last:
        count += 1
        last = x
    elif x + h < pairs[i + 1][0]:
        count += 1
        last = x + h
    else:
        last = x
        
print(count)