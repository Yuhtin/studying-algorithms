characters = list(input())
n = len(characters)

permutations = set()

def dfs(text, used):
    if len(text) == len(characters):
        permutations.add(text)
        return
    
    for i in range(n):
        if used[i]:
            continue
        if i > 0 and characters[i] == characters[i-1] and not used[i-1]:
            continue
        
        used[i] = True
        dfs(text + characters[i], used.copy())
        used[i] = False
    
dfs("", [False]*n)
print(len(permutations))
for i in permutations:
    print(i)