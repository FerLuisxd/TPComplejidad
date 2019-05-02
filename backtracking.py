#import funcionesPrincipales
import csv
from math import sin, cos, sqrt, atan2, radians
from itertools import permutations 
import datetime
from os import system
import time
import sys
sys.setrecursionlimit(300000)
start = time.time()

def Obtenerdata(data):
    with open('DatosReales.csv','r') as registros:
        lector = csv.reader(registros,delimiter=',')
        for fila in lector:
            CODCP = int(fila[0]) #Codigo de centro poblado (unico)
            DEP = fila[1]   #Departamento
            PROV = fila[2] #Provincia
            DIST = fila[3] #Distrito
            NOMCP = fila[4] #Nombre del centro poblado
            XCP = float(fila[5]) #Posicion X
            YCP = float(fila[6]) #Posicion Y
            data.append((CODCP, DEP, PROV, DIST, NOMCP, XCP, YCP))

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6
def calcularDistancia(x1,y1,x2,y2):        
    R = 6373.0  # approximate radius of earth in km
    lat1 = radians(y1) #y1
    lon1 = radians(x1) #x1
    lat2 = radians(y2)  #y2
    lon2 = radians(x2) #x2  
    dlon = lon2 - lon1 #Distancia entre longitudes
    dlat = lat2 - lat1 #Distancia entre latitudes   
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = R * c
    return distance

data =[]
Obtenerdata(data) 
print("Datos Leidos")


def departamentos(data):
    departamentos=[]
    departamentosName=[]
    for i in range(len(data)):
        if (data[i][dep] not in departamentosName):
            departamentos.append(data[i])
            departamentosName.append(data[i][dep])
    return departamentos

departamentos=departamentos(data)

#print(coordenadas)


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





array= btHandler(departamentos[:-19])
