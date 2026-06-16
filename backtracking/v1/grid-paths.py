n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    chars = list(input())
    for j in range(n):
        char = chars[j]
        if char == "*":
            grid[i][j] = -1
        
grid[0][0] = 1 # Start
grid[n-1][n-1] = 2 # Finish
        
def dfs(line, column):
    if line >= n or column >= n:
        return 0
    
    if line == n - 1 and column == n -1:
        return 1
    
    if grid[line][column] == -1:
        return 0
    
    return (
        dfs(line + 1, column)
        + dfs(line, column + 1)
    )

print(dfs(0, 0))