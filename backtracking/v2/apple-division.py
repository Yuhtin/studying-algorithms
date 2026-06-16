n, weights = int(input()), list(map(int, input().split()))
total = sum(weights)

def dfs(i, k):
    if i == n: return abs(k - (total - k))
    return min(dfs(i + 1, k + weights[i]), dfs(i + 1, k))

print(dfs(0, 0))