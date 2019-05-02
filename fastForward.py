

from calcDist import calcularDistancia

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6


#tomo de ejemplo a este gif
#https://camo.githubusercontent.com/d52cd6a47c7c0ee23ac107ad9b457101877ad489/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f322f32332f4e6561726573746e65696768626f722e676966

def fastForward(G,s):
    swap = G[s]
    G[s] = G[0]
    G[0]=swap
    dist=0
    sol=[]
    a=[]
    path=[]
    sol.append(G[0])
    for i in range(len(G)):
        menor=1000000000
        menorpos=i
        x=i+1
        for j in range(len(G)):
            if(j != i):
                if(j not in path):
                    if(menor>calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])):
                        menor=calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])
                        menorpos=j
        if(G[menorpos] not in sol):
            path.append(menorpos)
            dist=dist+menor
            sol.append(G[menorpos])
    for i in range(len(G)):
        if(i not in path):
            falta=i
    sol.append(G[falta])
    sol.append(G[0])
    dist=dist+calcularDistancia(G[0][xcp],G[0][ycp],G[falta][xcp],G[falta][ycp])
    print(sol)
    print(dist)
    a.append(sol)
    a.append(dist)
    return a