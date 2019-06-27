import time
import sys
import heapq as hq
from calcDist import calcularDistancia
start = time.time()

codcp = 0
dep  = 1
prov = 2
dist = 3
nomcp = 4
xcp = 5
ycp = 6

def TransformInfo(data):
    new = []
    for i in range(len(data)):
        for j in range(len(data)):
            if (i != j):
                new.append((calcularDistancia(data[i][xcp],data[i][ycp],data[j][xcp],data[j][ycp]),i,j))
    return new
      
def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa

def union(s, a, b):
    pa = find(s, a)
    pb = find(s, b)
    if pa == pb: return
    
    if s[pa] <= s[pb]:
        s[pa] += s[pb]
        s[pb] = pa
    elif s[pb] < s[pa]:
        s[pb] += s[pa]
        s[pa] = pb

def kruskal(data):
    lc = []
    td = 0
    il = TransformInfo(data)
    q = []
    n = len(data)
    for edge in il:
        hq.heappush(q, edge)
    roots = [-1]*n
    point = [0]*n
    T = []
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(roots, u) != find(roots, v) and point[v] < 2 and point[u] < 2:
            union(roots, u, v)
            T.append((u, v, w))
            td+=w
            point[u] += 1
            point[v] += 1
    for i in range(n):
        if (point[i] == 1):
            lc.append(i)
    union(roots, lc[0],lc[1])
    T.append((lc[0],lc[1],calcularDistancia(data[lc[0]][xcp],data[lc[0]][ycp],data[lc[1]][xcp],data[lc[1]][ycp])))
    td += calcularDistancia(data[lc[0]][xcp],data[lc[0]][ycp],data[lc[1]][xcp],data[lc[1]][ycp])        
    return td, T

def KruskallFixed(G):
    distance, T = kruskal(G)
    i = 0
    j = 0
    fixed = []
    done = [False]*len(T)
    fixed.append((T[0][0],T[0][1]))
    done[0] = True
    for i in range(len(T)):
        for j in range(len(T)):
            if fixed[i][1] == T[j][0] and done[j] == False:
                fixed.append((T[j][0],T[j][1]))
                done[j] = True
                break
            elif fixed[i][1] == T[j][1] and done[j] == False:
                fixed.append((T[j][1],T[j][0]))
                done[j] = True  
                break
            elif fixed[i][0] == T[j][0] and done[j] == False:
                fixed.append((T[j][0],T[j][1]))
                done[j] = True
                break
            elif fixed[i][0] == T[j][1] and done[j] == False:
                fixed.append((T[j][1],T[j][0]))
                done = True
                break
        if len(fixed) == len(T):
            break
    return distance, fixed    

def KruskallPrint(data):   #HANDLER
    json = []
    distancia, path = KruskallFixed(data)
    json.append(data[path[0][0]])
    json.append(data[path[0][1]])
    i=1
    while(i<len(path)):
        json.append(data[path[i][1]])
        i+=1
    return distancia, json    #DISTANCIA TOTAL, PATH


