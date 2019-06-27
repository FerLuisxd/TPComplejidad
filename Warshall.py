#import funcionesPrincipales
import time
import sys
from calcDist import calcularDistancia
sys.setrecursionlimit(300000)
start = time.time()

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

def floydWarshall(c,p,n):
    # n = len(G)
    # p = [[-1 for _ in range(n)]for _ in range(n)]
    # c = [[100000 for _ in range(n)]for _ in range(n)]
    # for u in range(n):
    #     for v, w in G[u]:
    #         p[u][v] = u
    #         c[u][v] = w
    
    for i in range(n):
        for u in range(n):
            for v in range(n):
                if i == u or i == v or u == v:
                    continue
                f = c[u][i] + c[i][v]
                if f < c[u][v]:
                    c[u][v] = f
                    p[u][v] = i
    return p, c

def minimun(G,c):
  
    thisD = 0
    solutionA = []
    pathA = []
    lastIndex = 1000
    n = len(c)
    
    onGoingA = True
    onGoing = True
    i = 0
    while onGoingA:
        n = len(c)
        solution = 0    
        path = []
        path.append(i)
        index = i
        while onGoing:
            menor = 100000000
            #index = i
            for j in range(n):
                if(index!=j):
                    if(j not in path):
                        if(menor>c[index][j]):
                            menor=c[index][j]
                            index = j
        
            solution = solution+menor
            path.append(index)
            if(len(path) == n):
                onGoing =False


        path.append(i)
        solution = solution + calcularDistancia(G[i][xcp],G[i][ycp],G[index][xcp],G[index][ycp])
        pathA.append(path)
        solutionA.append(solution)
        onGoing =True
        i = i +1
        if(len(pathA) == n):
            onGoingA=False


    # for i in range(n):
    #     thisD = 0
    #     lastIndex = 10000
    #     menor = 100000000
    #     for j in range(n):
    #         if(i!=j):
    #             if(j not in path):
    #                 if(menor>c[i][j])
    #             thisD = thisD + c[i][j]
    #             lastIndex = j
    #     lastD = calcularDistancia(G[i][xcp],G[i][ycp],G[lastIndex][xcp],G[lastIndex][ycp])
    #     thisD = thisD + lastD
    #     print(thisD)
    #     if(thisD<solution):
    #         solution=thisD
    print("solucion!!")
    print(solution)
    return solution
#3182.091627988606
def floydWarshallHandler(G):
    n = len(G)
    preal = [[-1 for _ in range(n)]for _ in range(n)]#path
    creal = [[100000 for _ in range(n)]for _ in range(n)]#cost
    for i in range(n):
        for j in range(n):
            if(i != j):
                thisD = calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])
                creal[i][j]=thisD
                preal[i][j]=i
                creal[j][i]=thisD
    # for i in range(n):
    #     string = str(i) + ' '
    #     for j in range(n):
    #         #if(i!=j):
    #         string = string + ' ' + str(creal[i][j])
    #     print(string)
    a,b = floydWarshall(creal,preal,n)
    print(a)
    #print(b)
    string = ''
    # for i in range(n):
    #     string = str(i) + ' '
    #     for j in range(n):
    #         #if(i!=j):
    #         string = string + ' ' + str(b[i][j])
    #     print(string)
    minimun(G,b)

G=[(683891, 'APURIMAC', 'GRAU', 'HUAYLLATI', 'Huamampallpa', -72.53126621, -13.99202976), (683892, 'JUNIN', 'SATIPO', 'RIO TAMBO', 'Campo Verde', -73.68263125, -11.23852662), (683894, 'ICA', 'ICA', 'LA TINGUI?æA', 'Sumac Wassi', -75.69002867, -14.0320047), (683896, 'CUSCO', 'PAUCARTAMBO', 'KOS?æIPATA', 'Selva Verde', -71.41628373, -12.93040825), (683897, 'TUMBES', 'ZARUMILLA', 'MATAPALO', 'Angel de la Luz', -80.25141478, -3.694722345), (683898, 'LIMA', 'LIMA', 'LURIGANCHO', 'Casa Huerta', -76.6739434, -11.91991169)]

floydWarshallHandler(G)