n = int(input())
pairs = list(tuple(map(int, input().split())) for _ in range(n))

pairs.sort(key=lambda x: x[1])

last = 0
for a, b in pairs:
    last += a
    if last > b:
        print("No")
        break
    
else:
    print("Yes")