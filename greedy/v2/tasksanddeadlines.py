n = int(input())
parts = list(tuple(map(int, input().split())) for _ in range(n))

parts.sort(key=lambda x: x[0])

total = 0
minutes = 0
for a, d in parts: 
    minutes += a
    total += d - minutes
    
print(total)