h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

used = []
def dfs(line, column):
    if line < 0 or column < 0 or line >= h or column >= w:
        return 0
    
    if line == h - 1 and column == w - 1:
        return 1
    
    if grid[line][column] in used:
        return 0
    
    used.append(grid[line][column])
    res = dfs(line + 1, column) + dfs(line, column + 1)
    used.pop()
    
    return res

print(dfs(0, 0))