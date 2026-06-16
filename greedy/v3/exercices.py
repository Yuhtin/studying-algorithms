from collections import Counter

# Movie Festival: https://cses.fi/problemset/task/1629
# Dado uma lista de filmes (inicio, fim), retorne o maximo de filmes que posso assistir sem sobrepor.
def max_movies(movies):
    movies.sort(key=lambda x: x[1])
    
    total = 0
    timestamp = 0
    for inicio, fim in movies:
        if inicio >= timestamp:
            total += 1
            timestamp = fim
    
    return total


# Ferris Wheel: https://cses.fi/problemset/task/1090
# Dado pesos e limite da gondola, retorne o menor numero de gondolas necessario.
def min_gondolas(weights, limit):
    n = len(weights)
    gondolas = 0
    
    weights.sort()
    
    left, right = 0, n - 1
    while left <= right:
        if weights[right] + weights[left] <= limit:
            left += 1

        right -= 1
        gondolas += 1

    return gondolas

# Megalomania: https://atcoder.jp/contests/abc131/tasks/abc131_d
# Dado trabalhos (duracao, deadline), retorne True se todos podem ser concluidos a tempo.
def can_finish_all_jobs(jobs):
    jobs.sort(key=lambda x: x[1])
    
    workedTime = 0
    for duracao, deadline in jobs:
        if workedTime + duracao > deadline:
            return False
        else:
            workedTime += duracao
        
    return True

# Tasks and Deadlines: https://cses.fi/problemset/task/1630
# Dado tarefas (duracao, deadline), retorne a soma total de (deadline - tempo_de_termino).
def total_reward(tasks):
    tasks.sort(key=lambda x: x[0])
    
    total = 0
    sum = 0
    for duracao, deadline in tasks:
        total += duracao
        sum += deadline - total
    
    return sum


# Woodcutters: https://codeforces.com/problemset/problem/545/C
# Dado arvores (posicao, altura), retorne o maximo de arvores que podem ser cortadas.
def max_cut_trees(trees):
    if not trees:
        return 0
    if len(trees) == 1:
        return 1

    total = 2
    max_x = trees[0][0]

    for i in range(1, len(trees) - 1):
        posicao, altura = trees[i]
        if posicao - altura > max_x:
            total += 1
            max_x = posicao
        elif posicao + altura < trees[i + 1][0]:
            total += 1
            max_x = posicao + altura
        else:
            max_x = posicao

    return total
            
    

# Taxi: https://codeforces.com/problemset/problem/158/B
# Dado grupos (tamanhos 1..4), retorne o menor numero de taxis necessario.
def min_taxis(group):
    groups = [0] * 5
    for value in group:
        groups[value] += 1
        
    mintaxis = groups[4]
    mintaxis += groups[3]
    groups[1] = max(0, groups[1] - groups[3])
    
    mintaxis += groups[2] // 2
    if groups[2] % 2:
        mintaxis += 1
        groups[1] = max(0, groups[1] - 2)
        
    if groups[1]:
        mintaxis += (groups[1] + 3) // 4
        
    return mintaxis

# Eating Candies: https://codeforces.com/problemset/problem/1669/F
# Dado um array de doces, retorne o maior total consumido com somas iguais dos dois lados.
def max_equal_candies(candies):
    n = len(candies)
    left, right = 0, n - 1
    sumleft, sumright = candies[0], candies[-1] 
    sum = 0
    
    while left < right:
        if sumleft == sumright:
            sum = left + 1 + n - right
            
            left += 1
            right -= 1
            sumleft += candies[left]
            sumright += candies[right]
        elif sumleft > sumright:
            right -= 1
            sumright += candies[right]
        elif sumright > sumleft:
            left += 1
            sumleft += candies[left]

    return sum

# Alternating Subsequence: https://codeforces.com/problemset/problem/1343/C
# Dado um array, retorne a maior soma de uma subsequencia com sinais alternados.
def max_alternating_sum(seq):
    sum = 0
    last = seq[0]
    
    for value in seq:
        if value * last < 0:
            sum += last
            last = value
        else:
            last = max(last, value)

    sum += last
    return sum 

def copa_do_mundo(jogadores, k):
    total = 0
    ganhos = []

    for ataque, defesa in jogadores:
        total += defesa
        ganhos.append(ataque - defesa)

    ganhos.sort(reverse=True)
    total += sum(ganhos[:k])

    return total
    
def _run_tests():
    tests = [
        (
            "max_movies",
            max_movies,
            [
                ([(3, 5), (4, 9), (5, 8)], 2),
                ([(1, 2), (2, 4), (4, 6)], 3),
                ([], 0),
                ([(5, 7), (1, 3), (3, 5), (2, 6)], 3),
                ([(0, 7), (2, 3), (3, 4), (4, 8)], 3),
            ],
        ),
        (
            "min_gondolas",
            min_gondolas,
            [
                (([3, 2, 2, 1], 3), 3),
                (([5, 1, 4, 2], 6), 2),
                (([1, 1, 1, 1], 2), 2),
                (([2, 2, 2], 3), 3),
                (([4], 5), 1),
            ],
        ),
        (
            "can_finish_all_jobs",
            can_finish_all_jobs,
            [
                ([(3, 9), (2, 8), (1, 5)], True),
                ([(4, 5), (3, 6)], False),
                ([(2, 2), (1, 100)], True),
                ([(5, 5)], True),
                ([(3, 3), (2, 4), (1, 5)], False),
            ],
        ),
        (
            "total_reward",
            total_reward,
            [
                ([(3, 10), (1, 2), (2, 6)], 8),
                ([(5, 5)], 0),
                ([(4, 7), (1, 100), (2, 5)], 101),
                ([(2, 2), (2, 2), (2, 2)], -6),
                ([], 0),
            ],
        ),
        (
            "max_cut_trees",
            max_cut_trees,
            [
                ([(1, 2), (2, 1), (5, 10), (10, 9)], 3),
                ([(1, 1), (2, 1)], 2),
                ([(5, 3)], 1),
                ([(1, 1), (2, 1), (3, 1)], 2),
                ([(1, 2), (4, 1), (6, 2), (10, 1)], 4),
            ],
        ),
        (
            "min_taxis",
            min_taxis,
            [
                ([1, 2, 4, 3, 3], 4),
                ([2, 3, 4, 4, 2, 1, 3, 1], 5),
                ([1, 1, 1, 1], 1),
                ([2, 2, 2, 2], 2),
                ([3, 1, 3, 1], 2),
                ([4, 4, 4], 3),
            ],
        ),
        (
            "max_equal_candies",
            max_equal_candies,
            [
                ([1, 2, 3, 3, 2, 1], 6),
                ([1, 1, 1, 1, 1, 1, 1], 6),
                ([10], 0),
                ([2, 1, 1, 2], 4),
                ([1, 3, 1], 2),
                ([1, 2, 1, 2, 1], 4),
            ],
        ),
        (
            "max_alternating_sum",
            max_alternating_sum,
            [
                ([1, 2, 3, -1, -2, -3, 4], 6),
                ([-1, -2, -3], -1),
                ([5], 5),
                ([1, 2, -5, -1, 4, 3], 5),
                ([1, -2, 3, -4, 5], 3),
                ([10, 9, 8], 10),
            ],
        ),
        (
            "copa_do_mundo",
            copa_do_mundo,
            [
                (([(10, 2), (3, 8), (7, 5), (1, 9)], 2), 34),
                (([(5, 1), (2, 6)], 1), 11),
                (([(1, 10), (2, 9), (3, 8)], 1), 22),
                (([(8, 1), (7, 2), (3, 9), (4, 10)], 3), 28),
                (([(6, 6), (5, 5), (1, 10), (10, 1)], 2), 31),
                (([(1000000000, 1), (1, 1000000000), (999999999, 2)], 2), 2999999999),
            ],
        ),
    ]

    total = 0
    passed = 0
    for name, fn, cases in tests:
        for args, expected in cases:
            total += 1
            result = fn(*args) if isinstance(args, tuple) else fn(args)
            if result == expected:
                passed += 1
                print(f"OK  {name} -> {result}")
            else:
                print(f"ERR {name} -> {result} (esperado {expected})")
    print(f"\nPassou {passed}/{total} testes")


if __name__ == "__main__":
    _run_tests()