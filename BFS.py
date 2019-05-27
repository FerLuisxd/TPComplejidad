from itertools import permutations 
import datetime
from calcDist import calcularDistancia
import time

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

def bfs(G, s):
    n = len(G)
    totalDistance=0
    visited = [False]*n
    queued = [False]*n
    queued[s] = True
    q = [s]
    cost=[]
    sol=[]
    allAdded=False  
    orden=[]
    while len(q) > 0:
        u = q[0]
        q = q[1:]
        if not visited[u]:
            visited[u] = True 
            orden.append(G[u])
            if(len(orden)>1):
                if(len(orden)<=n-1):
                    f = calcularDistancia(G[u][xcp],G[u][ycp],G[u-1][xcp],G[u-1][ycp])
                    totalDistance=totalDistance+f
                    cost.append(f)
            if(len(orden)==n):
                f= calcularDistancia(G[u][xcp],G[u][ycp],G[u-1][xcp],G[u-1][ycp])
                totalDistance=totalDistance+f
                cost.append(f)
                
                f = calcularDistancia(G[u][xcp],G[u][ycp],G[s][xcp],G[s][ycp])
                totalDistance=totalDistance+f
                cost.append(f)
                orden.append(G[s])
            if(not allAdded):
                allAdded = True
                for v in range(n):
                    if not queued[v]:  
                        queued[v] = True
                        q.append(v)            
    sol.append(orden) 
    sol.append(totalDistance)
    sol.append(cost)
    return sol

def handlerBfs(G,s):
    swap = G[s]
    G[s] = G[0]
    G[0]=swap
    
    solMenor=10000000000
    ordenSol=[]
    sol=[]
    start = time. time()
    rangoCambio=G[1:]
    cost=[]
    perm = permutations(rangoCambio) 
    for i in perm:
        esta = bfs([G[0]]+list(i),0)
        if(solMenor>=esta[1]):
            solMenor=esta[1]
            ordenSol=esta[0]
            cost=esta[2]
    end = time. time()
    print(end - start)
    print("Kms: " + str(solMenor))
    print(cost)
    sol.append(ordenSol)
    sol.append(solMenor)
    return sol