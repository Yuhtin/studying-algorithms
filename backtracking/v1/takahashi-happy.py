h, w = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]

def backtrack(line, column, path):
    # Outside of bounds, incorrect path
    if line >= h or column >= w or matrix[line][column] in path:
        return 0
    
    # Base Case, success
    if line == h - 1 and column == w - 1:
        return 1
    
    path.add(matrix[line][column])
    outcome = backtrack(line + 1, column, path) + backtrack(line, column + 1, path)
    path.remove(matrix[line][column])
    
    return outcome

# Usando set() porque o teste de "está no array?" é O(1)
print(backtrack(0, 0, set()))