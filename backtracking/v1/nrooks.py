n = int(input())
columns = [False]*n

def dfs(line):
    if line == n:        
        return 1
    
    res = 0
    for column in range(n):
        if not columns[column]:
            columns[column] = True
            res += dfs(line + 1)
            columns[column] = False
    
    return res

print(dfs(0))