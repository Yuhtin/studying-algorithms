n = int(input())
weights = list(map(int, input().split()))
total = sum(weights)

def solve(i, sum):
    if i == n:
        return abs(sum - (total - sum))
    
    # Primeira Decisão: Movo maça no indice i pro Grupo 1
    r1 = solve(i + 1, sum + weights[i])

    # Segunda Decisão: Movo maça no indice i pro Grupo 2
    r2 = solve(i + 1, sum)
    
    return min(r1, r2)
        
print(solve(0, 0))