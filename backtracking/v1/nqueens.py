class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [-1]*n
        solutions = []

        def formatBoard(unformatted):
            lines = []

            for line in range(n):
                string = ""
                for column in range(n):
                    if unformatted[line] == column:
                        string += "Q"
                    else:
                        string += "."

                lines.append(string)

            return lines

        def validate(line, column):
            if board[line] != -1:
                return False

            for checkLine in range(line):
                checkColumn = board[checkLine]
                if checkColumn == column:
                    return False

                diff_line = abs(line - checkLine)
                diff_column = abs(column - checkColumn)

                if diff_line == diff_column:
                    return False

            return True

        def backtrack(line):
            if line == n:
                # feasible solution
                # push board to solutions list
                solutions.append(formatBoard(board))
                return

            for column in range(n):
                if validate(line, column):
                    board[line] = column
                    backtrack(line + 1)
                    board[line] = -1

        backtrack(0)
        return solutions