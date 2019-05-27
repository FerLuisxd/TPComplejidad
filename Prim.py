


from itertools import permutations 
import datetime
from calcDist import calcularDistancia
import time
import heapq as hq
import math
INF = float("inf")

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6


def prim(G,s):   #Empieza en s
    print(G)
    n = len(G)
    Known = [False]*n
    Cost = [math.inf]*n
    Path = [-1]*n
    queue = []
    totalDistance=0
    Cost[s] = 0
    sol = []
    hq.heappush(queue, (0, s))#costo,pos
    while len(queue) > 0:
        _ , u = hq.heappop(queue)#costo,pos
        if not Known[u]:
            Known[u] = True
            for v, w in G[u]:#pos,costo
                if not Known[v] and w < Cost[v]:#si pos no conocida, costo menor al costo encontrado
                    Cost[v] = w
                    #totalDistance=totalDistance+w
                    Path[v] = u
                    hq.heappush(queue, (w, v))#costo,pos
    print(Cost)
    for i in range(len(Cost)):
        totalDistance=totalDistance+Cost[i]
    sol.append(Path)
    sol.append(totalDistance)
    return sol

#G =[(683892, 'JUNIN', 'SATIPO', 'RIO TAMBO', 'Campo Verde', -73.68263125, -11.23852662), (683894, 'ICA', 'ICA', 'LA TINGUI?æA', 'Sumac Wassi', -75.69002867, -14.0320047), (683896, 'CUSCO', 'PAUCARTAMBO', 'KOS?æIPATA', 'Selva Verde', -71.41628373, -12.93040825), (683897, 'TUMBES', 'ZARUMILLA', 'MATAPALO', 'Angel de la Luz', -80.25141478, -3.694722345), (683898, 'LIMA', 'LIMA', 'LURIGANCHO', 'Casa Huerta', -76.6739434, -11.91991169)]

def generarGrafito(G):
    u = len(G)
    x=[]
    for i in range(u):
        x.append([])
        for j in range(u):
            if(i!=j):
                x[i].append((j,calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])))
    return x

#def VerificarQueNoPasaPorCiudad:


def PrimHandler(G,s):
    swap = G[s]
    G[s] = G[0]
    G[0]=swap
    x = generarGrafito(G)
    esta = prim(x,0)#magia
    solMenor=10000000000
    #ordenSol=esta[0]
    ordenSol=[]
    for i in esta[0]:
        ordenSol.append(G[i])
    solMenor=esta[1]
    sol=[]

    print("Kms: " + str(solMenor))
    sol.append(ordenSol)
    sol.append(solMenor)
    return sol

#G = []
#with open('grafito.in') as f:
#    for line in f:
 #       u = len(G)
 #       G.append([])
 #       nums = [int(x) for x in line.split(' ')]
  #      for i in range(len(nums) // 2):
 #           G[u].append((nums[i * 2], nums[i * 2 + 1]))




#print(prim(G))



#q = []
