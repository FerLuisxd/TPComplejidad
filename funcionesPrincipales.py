import csv
import time
from math import sin, cos, sqrt, atan2, radians
from itertools import permutations 
import datetime
from os import system
from BruteForce import Comparing
from BFS import handlerBfs
from backtracking import btHandler
from fastForward import fastForward

def Obtenerdata():
    data = []
    with open('DatosReales.csv','r') as registros:
        lector = csv.reader(registros,delimiter=',')
        for fila in lector:
            CODCP = int(fila[0]) 
            DEP = fila[1]
            PROV = fila[2]
            DIST = fila[3]
            NOMCP = fila[4]
            XCP = float(fila[5])
            YCP = float(fila[6])
            data.append((CODCP, DEP, PROV, DIST, NOMCP, XCP, YCP))
    return data

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

data=Obtenerdata()

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

def distritoPorProvincia(provincia,data):
    distrito = []
    distritoName = []
    for i in range(len(data)):
        if(data[i][prov] == provincia):
            if(data[i][dist] not in distritoName):
                distrito.append(data[i])
                distritoName.append(data[i][dist])
    return distrito


def escribirEnJson(data,recorrido,km):
    now = datetime.datetime.now()
    filename= str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
    formate = "GeoJson-{}".format(filename)
    bien = str(formate)+".json"
    f = open(bien, "w")
    Recorridas=''
    for i in range(len(data)):
        Recorridas=Recorridas+' '+str((data[i][recorrido]))
    stringName=(str('{'+ '"Kms":' +str(km) +" ," + '"recorrido": "'+str(Recorridas)+'",\n'))
    f.write(stringName)
    stringBase=(str('"type": "FeatureCollection","features": [{"type": "Feature","properties": {},"geometry": {"type": "Polygon","coordinates": [[\n'))
    f.write(stringBase)
    for i in range(len(data)):
        f.write("["+str(data[i][xcp])+","+str(data[i][ycp])+"]")
        if(i<len(data)-1):
             f.write(",\n")
    f.write(']]}}]}')
    f.close()

def cli():
    print("Que desea hacer?")
    print("1)Departamentos")
    print("2)Provicia por Departamento(Ingresar nombre de departamento)")
    x=input('Ingrese opcion ')
    print(x)
    a = True
    b=[]
    if(x==str(1)):
            while(a):
                print("\033[H\033[J")
                print("Departamentos disponibles ")  
                for i in range(len(departamentos)):
                    if(departamentos[i] not in b):
                        print(str(i) + " " +str(departamentos[i][dep]))
                print("Departamentos cargados: ")
                for i in range(len(b)):
                    print(str(b[i]))
                print("Ingrese numero de departamento:")
                print("(X)Calcule distancia minima")
                print("(U)Vaciar departamentos cargados")
                v=input("Ingrese opcion ")
                if(v is not "X"):
                    for i in range(len(departamentos)):
                        if(str(i)==str(v)):
                            if(departamentos[i] not in b):
                                    b.append(departamentos[i])
                if(v=="U"):
                    b=[]
                if(v=="X"):
                    print("(S) Calcule distancia minima(BFS)")
                    print("(B) Calcule distancia minima(BackTracking)")
                    print("(F) Calcule distancia minima(Fuerza Bruta)")
                    print("(E) Calcula distancia minima(AlgoritmoRapido)")
                    v=input("Ingrese opcion ")
                    if(v=="S"):
                        arr = handlerBfs(b,0)
                        escribirEnJson(arr[0],dep,arr[1])
                        a=False
                    if(v=="B"):
                        arr = btHandler(b)
                        escribirEnJson(arr[0],prov,arr[1])
                        a=False
                    if(v=="F"):
                        arr = Comparing(b,0,dep)
                        escribirEnJson(arr[0][0],dep,arr[0][1])
                        a=False
                    if(v=="E"):
                        arr = fastForward(b,0)
                        escribirEnJson(arr[0],prov,arr[1])
                        a=False
                
                         
    if(x==str(2)):
        print("Departamentos disponibles: ")
        for i in range(len(departamentos)):
            print(str(i) + ") " +str(departamentos[i][dep]))
        name = input("Nombre del Departamento: ")
        provincia = provinciaPorDepartamento(name,data)
        print("A)Provincia por Departamento")
        print("B)Distrito por Provincia")
        c = input("Opcion: ")
        if (c == 'A'):
            while(a):
                system('clear')
                print("Departamento: ",name)
                print(" ")
                print(" ")
                print("Provincias Disponibles:")    
                for i in range(len(provincia)):
                    if provincia[i] not in b:
                        print(str(i)+ ") " + provincia[i][prov])
                print("Provincias Cargadas: ")
                for i in range(len(b)):
                    print(b[i][prov])                
                print("Ingrese numero de Provincia: ")            
                print("(X)Calcule distancia minima")
                print("(U)Vaciar Provincias cargadas")
                v=input("Ingrese opcion: ")
                if(v is not "X" and v is not "U"):
                    for i in range(len(provincia)):
                        if(str(i)==str(v)):
                            if(provincia[i] not in b):
                                b.append(provincia[i])

                if(v=="U"):
                    b=[]

                if(v=="X"):
                    print("(S) Calcule distancia minima(BFS)")
                    print("(B) Calcule distancia minima(BackTracking)")
                    print("(F) Calcule distancia minima(Fuerza Bruta)")
                    print("(E) Calcula distancia minima(AlgoritmoRapido)")
                    v=input("Ingrese opcion: ")
                    if(v=="S"):
                        arr = handlerBfs(b,0)
                        escribirEnJson(arr[0],prov,arr[1])
                        a = False
                    if(v=="B"):         
                        arr = btHandler(b)
                        escribirEnJson(arr[0],prov,arr[1])
                        a = False
                    if(v=="F"):
                        arr = Comparing(b,0,prov)
                        escribirEnJson(arr[0][0],prov,arr[0][1])
                        a=False
                    if(v=="E"):
                        arr = fastForward(b,0)
                        escribirEnJson(arr[0],prov,arr[1])
                        a=False
        if (c == 'B'):            
            print("Departamento: ",name)
            print("Provincias Disponibles:")    
            for i in range(len(provincia)):
                print(str(i)+ ") " + provincia[i][prov])
            x = input("Ingrese nombre de la Provincia: ")
            distrito = distritoPorProvincia(x,data)
            while(a):
                print("Departamento: ",name)
                print("Provincia: ", x)
                print(" ")
                print("Distritos Disponibles: ")
                for i in range(len(distrito)):
                        if distrito[i] not in b:
                            print(str(i)+ ") " + distrito[i][dist])
                print("Dsitritos Cargados: ")
                for i in range(len(b)):
                    print(b[i][dist])
                print("Ingrese numero de Distrito: ")            
                print("(X)Calcule distancia minima")
                print("(U)Vaciar distritos cargados")
                v=input("Ingrese opcion: ")
                if(v is not "X" and v is not "U"):
                    for i in range(len(distrito)):
                        if(str(i)==str(v)):
                            if(distrito[i] not in b):
                                b.append(distrito[i])
                
                if(v=="U"):
                    b=[]               
                if(v=="X"):
                    print("(S) Calcule distancia minima(BFS)")
                    print("(B) Calcule distancia minima(BackTracking)")
                    print("(F) Calcule distancia minima(Fuerza Bruta)")
                    print("(E) Calcula distancia minima(AlgoritmoRapido)")
                    v=input("Ingrese opcion: ")
                    if(v=="S"):
                        arr = handlerBfs(b,0)
                        escribirEnJson(arr[0],dist,arr[1])#Ingresas(DATOS_ARRAY,SI ES DEP O PROV O DIST, Kilometros)
                        a = False
                    if(v=="B"):    
                        arr = btHandler(b)     
                        escribirEnJson(arr[0],dist,arr[1])
                        a = False
                    if(v=="F"):
                        arr = Comparing(b,0,dist)
                        escribirEnJson(arr[0][0],dist,arr[0][1])
                        a=False
                    if(v=="E"):
                        arr = fastForward(b,0)
                        escribirEnJson(arr[0],prov,arr[1])
                        a=False
cli() 