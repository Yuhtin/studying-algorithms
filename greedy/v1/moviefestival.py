n = int(input())
parts = list(tuple(map(int, input().split())) for _ in range(n))

parts.sort(key=lambda x: x[1])

last = 0
max = 0
for a, b in parts:
    if last > a:
        continue
    
    last = b
    max += 1
    
print(max)