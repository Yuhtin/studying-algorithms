first = input()
second = input()

target = first.count("+") - first.count("-")
current = second.count("+") - second.count("-")
remaining = abs(target - current)

n = second.count("?")

def dfs(count, k):
    if count == n:        
        return 1 if k == target else 0
    
    if n - count < abs(target - k):
        return 0
    
    return dfs(count + 1, k + 1) + dfs(count + 1, k - 1)

print(dfs(0, current) / (2**n))