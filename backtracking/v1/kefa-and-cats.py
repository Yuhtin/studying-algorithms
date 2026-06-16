n, m = map(int, input().split())
vertex = [False]*(n+1)

second_line = list(input().split())
for i in range(len(second_line)):    
    if second_line[i] == "1":
        vertex[i+1] = True
    
connections = [[] for _ in range(n+1)]    

for i in range(1, n):
    x, y = map(int, input().split())
    connections[x].append(y)
    connections[y].append(x)

def dfs(root, parent, k):
    if vertex[root]:
        k += 1
    else:
        k = 0

    if k > m:
        return 0

    leaf = True
    total = 0

    for nxt in connections[root]:
        if nxt == parent:
            continue

        leaf = False
        total += dfs(nxt, root, k)

    return 1 if leaf else total

print(dfs(1, 0, 0))
