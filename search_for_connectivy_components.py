# Create simple example of adjacency matrix for graph
#     0 1 2 3 4 5 6 
M = [[0,0,0,0,1,0,0], # 0
     [0,0,1,0,0,0,0], # 1
     [0,1,0,0,0,0,0], # 2
     [0,0,0,0,1,0,1], # 3
     [1,0,0,1,0,0,0], # 4
     [0,0,0,0,0,0,0], # 5
     [0,0,0,1,0,0,0]  # 6
    ]

# search_for_connectivy_componenst
def poisk_cmp_sv(M):
    result = []
    n = len(M)
    for i in range(n):
        a = []
        a.append(i)
        for j in range(n):
            if M[i][j] == 1:
                a.append(j)
        f = 0
        for k in a:
            for g in result:
                if k in g:
                    f += 1
                    result[result.index(g)] = add(a, g)
        if f == 0:
            result.append(a)
    print(result)

# accessory function
def add(a, g):
    for i in a:
        if i not in g:
            g.append(i)
    return g


poisk_cmp_sv(M)
