characters = sorted(input())
n = len(characters)

permutations = []

def dfs(text, used):
    if len(text) == n:
        permutations.append(text)
        return

    for i in range(n):
        if used[i]:
            continue

        if i > 0 and characters[i] == characters[i-1] and not used[i-1]:
            continue

        used[i] = True
        dfs(text + characters[i], used)
        used[i] = False

dfs("", [False] * n)

print(len(permutations))
for p in permutations:
    print(p)