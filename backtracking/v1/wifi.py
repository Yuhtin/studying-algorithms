content = input()
decoded = input()

content_total = content.count("+") - content.count("-")
decoded_total = decoded.count("+") - decoded.count("-")
n = decoded.count("?")

def backtrack(i, curr):
    # Checar se é possível chegar na soma total (Bound)
    if abs(content_total - curr) > n - i:
        return 0
    
    # Chegamos ao fim 
    if i == n:
        # Retorna True se a soma for igual
        return 1 if curr == content_total else 0    
    
    # Somar o retorno da Decisão 1 e da Decisão 2
    # Decisão 1: Assumir que é +
    # Decisão 2: Assumir que é -
    return backtrack(i + 1, curr + 1) + backtrack(i + 1, curr - 1)        
        
# Começamos o backtracking com o que já sabemos da contagem de + e - conhecidos       
print(backtrack(0, decoded_total) / (2**n))