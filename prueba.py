from calcDist import calcularDistancia

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6
G =[(683892, 'JUNIN', 'SATIPO', 'RIO TAMBO', 'Campo Verde', -73.68263125, -11.23852662), (683894, 'ICA', 'ICA', 'LA TINGUI?æA', 'Sumac Wassi', -75.69002867, -14.0320047), (683896, 'CUSCO', 'PAUCARTAMBO', 'KOS?æIPATA', 'Selva Verde', -71.41628373, -12.93040825), (683897, 'TUMBES', 'ZARUMILLA', 'MATAPALO', 'Angel de la Luz', -80.25141478, -3.694722345), (683898, 'LIMA', 'LIMA', 'LURIGANCHO', 'Casa Huerta', -76.6739434, -11.91991169)]
def generarGrafito(G):
    u = len(G)
    x=[]
    for i in range(u):
        x.append([])
        for j in range(u):
            if(i!=j):
                x[i].append((j,calcularDistancia(G[i][xcp],G[i][ycp],G[j][xcp],G[j][ycp])))
    return x


a = generarGrafito(G)

l = len(a)
for i in range(l):
    stra =''
    for j in range(len(a[i])):
        stra= stra + str(a[i][j])
    print(stra)