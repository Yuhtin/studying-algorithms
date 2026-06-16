t = int(input())
for test in range(t):
    n = int(input())
    w = list(map(int, input().split()))
        
    best = 0
    maxCandies = 0
    left, right = 0, n - 1
    sumLeft, sumRight = w[left], w[right]
    
    while left < right:
        if sumLeft == sumRight:
            # quantos eu comi na esquerda + quantos comi na direita
            best = left + 1 + n - right

            left += 1
            sumLeft += w[left]
        elif sumLeft > sumRight:
            right -= 1
            sumRight += w[right]
        elif sumLeft < sumRight:
            left += 1
            sumLeft += w[left]
    
    print(best)