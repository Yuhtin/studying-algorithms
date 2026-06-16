class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(line, column, k):
            if line < 0 or column < 0 or line >= m or column >= n:
                return False

            if board[line][column] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            temp = board[line][column]
            board[line][column] = "#"
            
            res = (
                backtrack(line + 1, column, k + 1)
                or backtrack(line - 1, column, k + 1)
                or backtrack(line, column + 1, k + 1)
                or backtrack(line, column - 1, k + 1) 
            )
            
            board[line][column] = temp
            return res

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False