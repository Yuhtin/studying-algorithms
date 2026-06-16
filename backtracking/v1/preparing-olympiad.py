n, minimum, maximum, diff = map(int, input().split())
numbers = list(map(int, input().split()))

current = []

def backtrack(i, sum):
    if sum > maximum:
        return 0
    
    if i == n:
        return (
            len(current) >= 2
            and minimum <= sum <= maximum
            and max(current) - min(current) >= diff
        )
    
    current.append(numbers[i])
    # Decisão 1: selecionar o problema
    ans = backtrack(i + 1, sum + numbers[i])
    
    current.pop()
    # Decisão 2: não selecionar o problema
    ans += backtrack(i + 1, sum)
    
    return ans
    
print(backtrack(0, 0))