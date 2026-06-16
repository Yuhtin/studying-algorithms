class Solution:
    def totalNQueens(self, n: int) -> int:
        tabuleiro = [-1]*n

        def backtracking(linha):
            if linha == n:
                return 1

            solucoes = 0

            for coluna in range(n):
                if isValid(linha, coluna):
                    tabuleiro[linha] = coluna
                    solucoes += backtracking(linha + 1)
                    tabuleiro[linha] = -1

            return solucoes

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