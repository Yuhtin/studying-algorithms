class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        x, y = 0, 0
        empty = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] != -1:
                    empty += 1

        def backtrack(line, column, walked):            
            if line < 0 or line >= m or column < 0 or column >= n:
                return 0
            
            if grid[line][column] == -1:
                return 0

            if grid[line][column] == 2:
                return 1 if empty == walked else 0

            grid[line][column] = -1
            
            total = backtrack(line + 1, column, walked + 1) + backtrack(line, column + 1, walked + 1) + backtrack(line - 1, column, walked + 1) + backtrack(line, column - 1, walked + 1)

            grid[line][column] = 0

            return total
        
        return backtrack(x, y, 1)