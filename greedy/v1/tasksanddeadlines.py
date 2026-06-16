n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]

pairs.sort(key=lambda x: x[0])

maxreward = 0
time = 0
for duration, deadline in pairs:
    time += duration
    maxreward += deadline - time
    
print(maxreward)