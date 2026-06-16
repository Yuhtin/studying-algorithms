n, x = tuple(map(int, input().split()))
childs = list(map(int, input().split()))

childs.sort()

left, right = 0, n - 1
count = 0
while left <= right:
    if left != right and childs[left] + childs[right] <= x:
        left += 1

    right -= 1
    count += 1
        
print(count)