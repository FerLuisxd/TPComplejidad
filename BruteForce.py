from itertools import permutations
from calcDist import calcularDistancia
import time

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6
inf = 9999999

def Change(data, node):
    aux = data[node]
    data[node] = data[0]
    data[0] = aux
    return data    

def BruteForce(G):   
    Solution = []
    r = len(G)
    i = 0
    distancia = 0
    while(i<r):
        if i!=r-1:
            distancia = distancia + calcularDistancia(G[i][xcp],G[i][ycp],G[i+1][xcp],G[i+1][ycp])
        else:
            distancia = distancia + calcularDistancia(G[i][xcp],G[i][ycp],G[0][xcp],G[0][ycp])
        i=i+1
        
        
    Solution.append((G+[G[0]],distancia))
    return Solution

def Comparing(G,start,tipo):    
    Change(G,start)
    perm = permutations(G[1:])
    possible = []
    path = []
    menor = 999999
    for p in perm:
        possible = BruteForce([G[0]]+list(p))
        if menor > possible[0][1]:
            path = possible
            menor = path[0][1]
    for i in range(len(path[0][0])-1):
        print(str(path[0][0][i][tipo]),"->",str(path[0][0][i+1][tipo]))     
    print("Distancia: ", path[0][1])
    end = time. time()
    print("Tiempo: ", end - start)
    return path