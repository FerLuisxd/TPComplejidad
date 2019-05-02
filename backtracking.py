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



def bt(G,pos,conf,distancias,path,used,N):
    if(pos==-1):
        total = 0
        for i in range(N):
            pos1=conf[i]
            pos2=conf[(i+1)%N]
            total+=calcularDistancia(G[pos2][xcp],G[pos2][ycp],G[pos1][xcp],G[pos1][ycp])
        distancias.append(total)    
        #print(distancias)
        auxpath=[]
        for i in range(N):
            auxpath.append(conf[i])
        path.append(auxpath)
        return
    for i in range(N):
        if(used[i]==0):
            used[i]=1
            conf[pos]=i
            bt(G,pos-1,conf,distancias,path,used,N)
            used[i]=0
            conf[pos]=-1

def btHandler(G):
    N = len(G)
    print(N)
    used = [0]*N
    conf = [-1]*N
    distancias=[]
    path =[]     
    bt(G,N-1,conf,distancias,path,used,N)
    ans=1000000000
    pans=[-1]*N
    for i in range(len(distancias)):
        if(distancias[i]<ans):
            ans=distancias[i]
            #print(ans)
            pans=path[i]
    pans.append(pans[0])
    sol=[]
    b=[]
    for i in range(N):
        for j in range(N):
            if(j==pans[i]):
                if(G[i]not in b):
                    b.append(G[i])
    b.append(G[0])  
    sol.append(b)
    sol.append(ans)
    #print(sol)
    end = time.time()
    print(end-start)
    return sol





#array= btHandler(departamentos[:-19])
