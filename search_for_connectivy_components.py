# Пример матрицы смежности для случайного графа.
#     0 1 2 3 4 5 6 
M = [[0,0,0,0,1,0,0], # 0
     [0,0,1,0,0,0,0], # 1
     [0,1,0,0,0,0,0], # 2
     [0,0,0,0,1,0,1], # 3
     [1,0,0,1,0,0,0], # 4
     [0,0,0,0,0,0,0], # 5
     [0,0,0,1,0,0,0]  # 6
    ]


# Поиск компонентов связности
def poisk_cmp_sv(M):
    result = []
    n = len(M)
    for i in range(n):
        a = []
        a.append(i)
        for j in range(n):
            if M[i][j] > 0:
                a.append(j)
        f = 0
        for k in a:
            for g in result:
                if k in g:
                    f += 1
                    result[result.index(g)] = add(a, g)
        if f == 0:
            result.append(a)
    return check(result)
def add(a, g):
    for i in a:
        if i not in g:
            g.append(i)
    return g
def check(result):
    n = len(result)
    for i in range(n):
        for j in range(len(result[i])):
            f = 0
            for k in range(i+1, n):
                if result[i][j] in result[k]:
                    result[k] = add(result[i], result[k])
                    result[i] = 'err'
                    f = 1
                    break
            if f == 1:
                break
    while 'err' in result:
        result.remove('err')
    return result
