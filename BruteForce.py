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
inf = 9999999

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

def Comparing(G,start):    
    Change(G,start)
    perm = permutations(G[1:])
    possible = []
    path = []
    menor = inf
    start = time.time()
    for p in perm:
        possible = BruteForce([G[0]]+list(p))
        if menor > possible[0][1]:
            path = possible
            menor = path[0][1]

    for i in range(len(path[0][0])-1):
        print(str(path[0][0][i][dep]),"->",str(path[0][0][i+1][dep]))
        
    print("Distancia: ", path[0][1])
    end = time. time()
    print(end - start)