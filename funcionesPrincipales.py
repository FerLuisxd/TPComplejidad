

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

def calcularDistancia(y1,x1,x2,y2):
    # approximate radius of earth in km
    R = 6371e3 #metros a km?

    lat1 = radians(y1)
    lon1 = radians(x2)
    lat2 = radians(y2)
    lon2 = radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance #retorna distancia
    #print("Result:", distance)
    #print("Should be:", 278.546, "km")

data=[]
Obtenerdata(data)
print(data)

