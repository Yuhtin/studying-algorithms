n = int(input())

columns = []

def dfs(line):
    if line == n:        
        return 1
    
    res = 0
    for column in range(n):
        if column not in columns:
            columns.append(column)
            res += dfs(line + 1)
            columns.pop()
    
    return res

print(dfs(0))