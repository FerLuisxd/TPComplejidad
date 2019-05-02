#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import funcionesPrincipales
import time
import sys
sys.setrecursionlimit(3000)
start = time.time()

coordenadas = [(departamentos[0][xcp],departamentos[0][ycp]),
              (departamentos[1][xcp],departamentos[1][ycp]),
              (departamentos[2][xcp],departamentos[2][ycp]),
              (departamentos[3][xcp],departamentos[3][ycp]),
              (departamentos[4][xcp],departamentos[4][ycp]),
              (departamentos[5][xcp],departamentos[5][ycp]),
              (departamentos[6][xcp],departamentos[6][ycp]),
              (departamentos[7][xcp],departamentos[7][ycp]),
              (departamentos[8][xcp],departamentos[8][ycp]),
              (departamentos[9][xcp],departamentos[9][ycp])]

#print(coordenadas)
N = len(coordenadas)
print(N)
used = [0]*N
conf = [-1]*N

distancias=[]
path =[]

def bt(pos):
    if(pos==-1):
        total = 0
        for i in range(N):
            pos1=conf[i]
            pos2=conf[(i+1)%N]
            total+=calcularDistancia(coordenadas[pos2][0],coordenadas[pos2][1],coordenadas[pos1][0],coordenadas[pos1][1])
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
            bt(pos-1)
            used[i]=0
            conf[pos]=-1
            
bt(N-1)
ans=1000000000
pans=[-1]*N
for i in range(len(distancias)):
    if(distancias[i]<ans):
        ans=distancias[i]
        #print(ans)
        pans=path[i]
pans.append(pans[0])
print(ans,pans)
end = time.time()
print(end-start)

