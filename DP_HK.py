import itertools
from calcDist import calcularDistancia
import time
codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

def HK(G):
    start = time. time()
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
    end = time. time()
    print("Tiempo de ejecución: " + str(end - start))
    print("Km recorridos: " + str(opt))
    sitios = G
    sitios.append(G[0])
    sol = []
    sol.append(sitios)
    sol.append(opt) #costo
    sol.append(list(reversed(path))) #camino
    return sol#, list(reversed(path)) #costo, camino

#G=[(683892, 'JUNIN', 'SATIPO', 'RIO TAMBO', 'Campo Verde', -73.68263125, -11.23852662), (683894, 'ICA', 'ICA', 'LA TINGUI?æA', 'Sumac Wassi', -75.69002867, -14.0320047), (683896, 'CUSCO', 'PAUCARTAMBO', 'KOS?æIPATA', 'Selva Verde', -71.41628373, -12.93040825), (683897, 'TUMBES', 'ZARUMILLA', 'MATAPALO', 'Angel de la Luz', -80.25141478, -3.694722345), (683898, 'LIMA', 'LIMA', 'LURIGANCHO', 'Casa Huerta', -76.6739434, -11.91991169)]

#a = HK(G)
#print(a[1])