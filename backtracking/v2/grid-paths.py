n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(input())
    for j in range(len(line)):
        if line[j] == "*":
            grid[i][j] = -1
            
def dfs(line, column):
    if line >= n or column >= n:
        return 0
    
    if grid[line][column] == -1:
        return 0
    
    if line == n -1 and column == n -1:
        return 1
    
    return dfs(line + 1, column) + dfs(line, column + 1)

print(dfs(0, 0))