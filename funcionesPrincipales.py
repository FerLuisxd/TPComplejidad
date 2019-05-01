

import csv
from math import sin, cos, sqrt, atan2, radians

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
Obtenerdata(data) #dsda


print(data[0][xcp],data[0][ycp])
print(data[1][xcp],data[1][ycp])
print(calcularDistancia(data[0][xcp],data[0][ycp],data[1][xcp],data[1][ycp]))


def departamentos(data):
    departamentos=[]
    departamentosName=[]
    for i in range(len(data)):
        if (data[i][dep] not in departamentosName):
            departamentos.append(data[i])
            departamentosName.append(data[i][dep])
    return departamentos

departamentos=departamentos(data)

print(departamentos)
print(len(departamentos))

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

def bfs(G, s,orden):
    n = len(G)
    totalDistance=0
    visited = [False]*n
    queued = [False]*n#???
    #orden = []
    queued[s] = True
    q = [s]#0
    for i in range(len(orden)):
         if(i>=1):
                if(i<=24):
                    totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[u-1][xcp],G[u-1][ycp])
        if(i==25):
                totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[0][xcp],G[0][ycp])
    while len(q) > 0:
        u = q[0]#0
        q = q[1:]#nada y se va 0
        if not visited[u]:#0
            visited[u] = True
            #orden[0] #accedemos 0
            if(len(orden)>1):
                if(len(orden)<=24):
                    totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[u-1][xcp],G[u-1][ycp])
            if(len(orden)==25):
                totalDistance=totalDistance+calcularDistancia(G[u][xcp],G[u][ycp],G[0][xcp],G[0][ycp])
            
    
    # 0 1 2 3 4 5
    

    print(totalDistance)
    print(orden)

orden = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0]
bfs(departamentos,0,orden)