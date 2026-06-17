class Solution:
    def totalNQueens(self, n: int) -> int:
        tabuleiro = [-1]*n

        def backtracking(linha):
            if linha == n:
                return True

            for coluna in range(n):
                if tabuleiro[linha][coluna] == "*":
                    continue
                
                if isValid(linha, coluna):
                    tabuleiro[linha] = coluna
                    if backtracking(linha + 1):
                        return True
                    
                    tabuleiro[linha] = -1

            return False

        def isValid(linha, coluna):
            for line in range(linha):
                column = tabuleiro[line]

                if column == coluna:
                    return False

                dist_linhas = abs(linha - line)
                dist_colunas = abs(coluna - column)

                if dist_linhas == dist_colunas:
                    return False

            return True

        return backtracking(0)