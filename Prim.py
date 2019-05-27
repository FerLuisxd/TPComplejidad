

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

def Prim(G,s):
    swap = G[s]
    G[s] = G[0]
    G[0]=swap
    dist=0
    sol=[]
    nexti=[]
    nexti.append(0)
    a=[]
    path=[]
    path.append(0)
    sol.append(G[0])
    costo=[]
    for i in range(len(G)-1):
        menor=1000000000
        menorpos=i
        xy=nexti[len(nexti)-1]
        for j in range(len(G)):
            #if(j != i):
                if(j not in path):
                    f=calcularDistancia(G[xy][xcp],G[xy][ycp],G[j][xcp],G[j][ycp])
                    if(menor>f and f is not 0.0):
                        menor=f
                        menorpos=j
        path.append(menorpos)
        dist=dist+menor
        nexti.append(menorpos)
        sol.append(G[menorpos])
        costo.append(menor)
    wa= path[len(path)-1]
  #  if(costo[len(costo)-1]==996.0691874058272):
  #      print(a)
    path.append(0)
    sol.append(G[0])
    cost = calcularDistancia(G[0][xcp],G[0][ycp],G[wa][xcp],G[wa][ycp])
    dist=dist+cost
    costo.append(cost)
    #print(sol)
    #print(dist)
    a.append(sol)
    a.append(dist)
    a.append(path)
    a.append(costo)
    return a

def PrimHandler(G):
    x=[]
    menor =1000000
    sol=0
    path=0
    for i in range(len(G)):
        a =Prim(G,i)
        if(menor>a[1]):
            menor=a[1]
            sol=a[0]
            path=a[2]
            cost=a[3]
    
    realsol=[]
    realsol.append(sol)
    realsol.append(menor)
    
    realsol.append(path)
    realsol.append(cost)
    return realsol


#G=[(683892, 'JUNIN', 'SATIPO', 'RIO TAMBO', 'Campo Verde', -73.68263125, -11.23852662), (683894, 'ICA', 'ICA', 'LA TINGUI?æA', 'Sumac Wassi', -75.69002867, -14.0320047), (683896, 'CUSCO', 'PAUCARTAMBO', 'KOS?æIPATA', 'Selva Verde', -71.41628373, -12.93040825), (683897, 'TUMBES', 'ZARUMILLA', 'MATAPALO', 'Angel de la Luz', -80.25141478, -3.694722345), (683898, 'LIMA', 'LIMA', 'LURIGANCHO', 'Casa Huerta', -76.6739434, -11.91991169)]

#PrimHandler(G)