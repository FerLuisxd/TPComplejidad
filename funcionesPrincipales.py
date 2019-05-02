

import csv
import time
from math import sin, cos, sqrt, atan2, radians
from itertools import permutations 

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

print("Que desea hacer?")
print("1)Departamentos")
print("2)Provicia por Departamento(Ingresar nombre de departamento)")

#input(a)

def departamentos(data):
    departamentos=[]
    departamentosName=[]
    for i in range(len(data)):
        if (data[i][dep] not in departamentosName):
            departamentos.append(data[i])
            departamentosName.append(data[i][dep])
    return departamentos

departamentos=departamentos(data)

def provinciaPorDepartamento(nombre,data):
    provincias=[]
    provinciaName=[]
    for i in range(len(data)):
        if(data[i][dep]==nombre):
            if (data[i][prov] not in provinciaName):
                provincias.append(data[i])
                provinciaName.append(data[i][prov])
    return provincias

provinciasAmazonas=provinciaPorDepartamento("AMAZONAS",data)   

def distritoPorProvincia(provincia,data):
    distrito = []
    distritoName = []
    for i in range(len(data)):
        if(data[i][prov] == provincia):
            if(data[i][dist] not in distritoName):
                distrito.append(data[i])
                distritoName.append(data[i][dist])
    return distrito


def dfs(G, s):
    n = len(G)
    visited = [False]*n
    queued = [False]*n
    queued[s] = True
    q = [s]
    while len(q) > 0:
        u = q.pop()
        if not visited[u]:
            visited[u] = True
            print(u)
            for v in reversed(G[u]):
                if not queued[v]:
                    queued[v] = True
                    q.append(v)

def bfs(G, s):
    n = len(G)
    totalDistance=0
    visited = [False]*n
    queued = [False]*n
    queued[s] = True
    q = [s]
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
                    totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[u-1][xcp],G[u-1][ycp])
            if(len(orden)==n):
                totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[s][xcp],G[s][ycp])
                orden.append(G[s])
            if(not allAdded):
                allAdded = True#recorrido del grafo se selecciona el camino aqui
                for v in range(n):#hace for a veces que no debe
                    if not queued[v]:  
                        queued[v] = True
                        q.append(v)            
    sol.append(orden)#guardar nombres 
    sol.append(totalDistance)
    return sol

#       start = time. time()
#print(bfs(departamentos,0))
#nd = time. time()
#print(end - start)

def handlerBfs(G,s):
    rangoCambio=G[1:]
    #posiblidades=[]
    solMenor=10000000000
    ordenSol=[]
    n = len(G)
    perm = permutations(rangoCambio) 
    f=0
    start = time. time()
# Print the obtained permutations 
    for i in perm:
        esta = bfs([G[s]]+list(i),s)
        if(solMenor>=esta[1]):
            solMenor=esta[1]
            ordenSol=esta[0]
       # bfs(G[0]+perm(i),s)        
    #bfs(perm(i)) #orden # n = 24
   # f=f+1#aca entra a trabajar
    end = time. time()
    print("HandleBFS")
    print(solMenor)
    for i in range(len(ordenSol)):
        print(ordenSol[i][dep])
    #print(f)
    
    print(end - start)

    #for i in range(n):

#print(len(departamentos[:-15]))
handlerBfs(departamentos,0)