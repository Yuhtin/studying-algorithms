t = int(input())
for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    
    sum = 0
    tempMax = values[0]
    negative = values[0] < 0
    for i in range(1, n):
        # positive
        if values[i] > 0:
            if negative:
                # flipped
                sum += tempMax
                tempMax = values[i]
                negative = False
            else: # it was already positive
                # not flipped, update highest
                tempMax = max(values[i], tempMax)                
        else: # is negative
            if negative: # stayed negative
                # not flipped, update highest
                tempMax = max(values[i], tempMax)                
            else:
                # flipped
                sum += tempMax
                tempMax = values[i]
                negative = True
                
    sum += tempMax
    print(sum)