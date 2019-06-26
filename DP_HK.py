import itertools
from calcDist import calcularDistancia

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

def HK(G):
    global n
    n = len(G)
    distancias = [[0] * n for i in range(n)]
    for i in range (n):
        for j in range(i+1, n):
            distancias[i][j] = distancias[j][i] = calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])

    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (distancias[0][k], 0)
    for _ in range(2, n):
        for subs in itertools.combinations(range(1, n), _): #todos los subconjuntos posibles
            bits = 0
            for bit in subs:
                bits |= 1 << bit
            for k in subs:
                prev = bits & ~(1 << k)
                res = []
                for m in subs:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distancias[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distancias[k][0], k))
    opt, padre = min(res)
    path = []
    for i in range(n - 1):
        path.append(padre)
        new_bits = bits & ~(1 << padre)
        _, padre = C[(bits, padre)]
        bits = new_bits

    path.append(0)

    return opt, list(reversed(path)) #costo, camino