n = int(input())

groups = [0] * 5
for value in list(map(int, input().split())):
    groups[value] += 1
    
cnt = groups[4]

cnt += groups[3]
groups[1] = max(0, groups[1] - groups[3])

cnt += groups[2] // 2

if groups[2] % 2:
    cnt += 1
    groups[1] = max(0, groups[1] - 2)    
    
if groups[1]:    
    cnt += (groups[1] + 3) // 4

print(cnt)