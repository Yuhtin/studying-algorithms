n = int(input())
inputs = [tuple(map(int, input().split())) for _ in range(n)]

inputs.sort(key=lambda x: x[1])

timeWorked = 0
for units, deadline in inputs:
    timeWorked += units
    if timeWorked > deadline:
        print("No")
        break
else:
    print("Yes")