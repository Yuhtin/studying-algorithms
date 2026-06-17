n, minimum, maximum, diff = map(int, input().split())
numbers = list(map(int, input().split()))

current = []

def dfs(i, k):
    if k > maximum:
        return 0        
    
    if i == n:
        return (
            k > 0
            and max(current) - min(current) >= diff
            and k >= minimum
        )
    
    current.append(numbers[i])
    # Take
    res = dfs(i + 1, k + numbers[i])
    
    current.pop()
    # Don't Take
    res += dfs(i + 1, k)
    return res
    
print(dfs(0, 0))