# Travelling Salesman Problem (TSP) / Problema del vendedor viajante

El problema del vendedor viajante (TSP por sus siglas en inglés) consiste en resolver la siguiente interrogante: ¿cuál es la ruta
más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?

Este problema se encuentra clasificado como problema de optimización combinatoria; es decir, un problema el el cual intervienen cierto número de variables, donde cada una puede tener N diferentes valores y cuyo número de combinaciones es de carácter exponencial. Ello da lugar a múltiples soluciones óptimas (soluciones que se calculan en un tiempo finito) para una instancia.

En el contexto de nuestro problema, utilizamos como ciudades a los centros poblados del Perú.

   [![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)

# Nuestra propuesta
La solución al problema presentado representa un desafío, ya que, actualmente, no es posible dar una solución óptima en un tiempo razonable al TSP. Sin embargo, nuestro objetivo no es dar una solución total, sino una parcial; es decir, lograr una ruta coherente y, a la vez, lograr un tiempo de ejecución reducido. En ese sentido, solo es posible solucionar el problema en tiempos de cómputo pequeños cuando utilizamos un número pequeño de elementos. Además, cabe resaltar que consideramos todos los centros poblados conectados entre sí; es decir, existe un camino de un punto hacia cualquier otro.
En nuestro caso, los algoritmos que aplicaremos son: fuerza bruta, backtracking y BFS.


# Objetivos:

- Implementar soluciones parciales al problema del viajero utilizando solamente algoritmos de búsqueda.
- Analizar y comprender la complejidad de cada algoritmo aplicado.
- Representar la solución de manera gráfica y permitir la interacción del usuario a través de una interfaz.

# Marco Teorico

 - Fuerza Bruta:
    >Es un algoritmo que no implementa atajos para mejorar el rendimiento. Por el contrario, se encarga de probar todas las     posibilidades sistemáticamente hasta hallar la solución.
    
   [![](https://upload.wikimedia.org/wikipedia/commons/2/23/Nearestneighbor.gif)](https://upload.wikimedia.org/wikipedia/commons/2/23/Nearestneighbor.gif)
   
   
- Backtracking:
    >Es un algoritmo que consiste en recursión intensiva para resolver problemas por etapas, que utiliza como árbol de decisiones la propia organización de la recursión. Cuando se “avanza” de etapa se realiza una llamada recursiva, y cuando se “retrocede” lo que
se hace es terminar el correspondiente proceso recursivo, con lo que efectivamente se vuelve al estado anterior por la pila de entornos creada en la recursión. 

   [![](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)
   
   
 - BFS:
    >Es un algoritmo que consiste en un recorrido transversal de los elementos (si se visualiza como un árbol). Recorre todos los elementos del mismo nivel, y luego desciende al siguiente nivel y continúa el recorrido de manera transversal.

   [![](https://i.imgur.com/kxETgI0.png)](https://i.imgur.com/kxETgI0.png)
   
 - Prim:
    >Es un algoritmo que encuentra un subconjunto de aristas que forman un árbol con todos los vértices, donde el peso total de todas las aristas en el árbol es el mínimo posible.
    
  [![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)
   
   
- Programación dinámica (Algoritmo de Held-Karp):
    >Es un algoritmo que consiste en calcular el menor costo a través de subconjuntos de nodos reutilizando las soluciones previamente calculadas, que es la característica principal de la programación dinámica.

   ![](https://cdn-images-1.medium.com/max/1600/1*c5cw35mBFfgzn_T9LOh3zA.jpeg)
   
   
 - Kruskal:
    >Es un algoritmo que consiste en tomar la arista de menor peso y continuar mientras no se formen ciclos.
   ![](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Prims-and-Kruskals-Algorithm.png)


# Complejidad de las estrategias

[![](http://4.bp.blogspot.com/-UoorZCAsVhM/T8F-_8210LI/AAAAAAAAADI/xGCK5B0y8CQ/s1600/Imagen1.png)](http://4.bp.blogspot.com/-UoorZCAsVhM/T8F-_8210LI/AAAAAAAAADI/xGCK5B0y8CQ/s1600/Imagen1.png)
- Complejidad Solucion 1: (Backtracking)
 >La complejidad es de n!, pues prueba todas las permutaciones posibles para hallar el ciclo más óptimo
 
    ```
    for i in range(N): 
      if(used[i]==0): 
        used[i]=1 
        conf[pos]=i 
        bt(pos-1) 
        used[i]=0 
        conf[pos]=-1

    ```
- Complejidad Solucion 2: (BFS)
 >Podemos ver que la complejidad es de (n-1)! ya que esta debe recorrer todos las permutaciones creadas para asi descubrir la solucion
 >con menores kilometros
 ```
   rangoCambio=Arreglo[1:]         
   perm = permutations(rangoCambio) 
   for i in perm: 		    	
   	esta = bfs([Arreglo[0]]+list(i),0)
   	if(solMenor>=esta[1]):
		solMenor=esta[1]
		ordenSol=esta[0]
   ```
- Complejidad Solucion 3: (Fuerza Bruta)
 >Podemos ver que la complejidad es de (n-1)! ya que esta debe recorrer todos las permutaciones creadas para asi descubrir la solucion
 >con menores kilometros
 ```
 
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
   ```
 - Complejidad Solucion 4: (Prim)
 >Esta solucion usa el algoritmo prim en todos los puntos iniciales, obteniendo el arbol de expansion mas corto que regresa al punto de inicio, el algoritmo prim es en si n*log(n) pero como lo debemos comparar con todos los puntos de inicio es n^2*log(n) 
 ```
for i in range(len(G)-1):#-1 porque el ultimo sabemos que es del punto final al inicio.
        menor=1000000000
        menorpos=i
        xy=nexti[len(nexti)-1]
        for j in possibleWays:
                    f=calcularDistancia(G[xy][xcp],G[xy][ycp],G[j][xcp],G[j][ycp])
                    if(menor>f and f is not 0.0):
                        menor=f
                        menorpos=j
        path.append(menorpos)
        dist=dist+menor
        nexti.append(menorpos)
        sol.append(G[menorpos])
        costo.append(menor)
        possibleWays.remove(menorpos)
    wa= path[len(path)-1]
    path.append(0)
    sol.append(G[0])
    cost = calcularDistancia(G[0][xcp],G[0][ycp],G[wa][xcp],G[wa][ycp])
    dist=dist+cost
   ```
   - Complejidad Solucion 5: (Programación Dinámica)
 >Esta solución, que emplea el algoritmo de Held-Karp, calcula todos los posibles subconjuntos, la cual es una cantidad exponencial 2^n. Además, por cada subconjunto. Además, en cada subconjunto se hace un recorrido a través de cada vértice y se comprueba el mejor orden de los mismos. Por lo tanto, resulta en una complejidad de (n^2)*(2^n)
 ```
 for _ in range(2, n):
        for subs in itertools.combinations(range(1, n), _): #todos los subconjuntos posibles
            bits = 0
            for bit in subs:
                bits |= 1 << bit
            for k in subs:
                prev = bits & ~(1 << k)
                res = []
                for m in subs:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distancias[m][k], m))
                C[(bits, k)] = min(res)
 
   ```
# Conclusiones

  - Los algoritmos de búsqueda exhaustiva (y también Held-Karp) pueden requerir un tiempo de computación astronómico si emplean un           elevado número de elementos.
  - Los algoritmos de búsqueda (y también Held-Karp) pueden hallar la solución correcta para un grupo pequeño de elementos, pero no de       la forma más óptima.
  - Los algoritmos que ofrecen una solución medianamente óptima, emplean un tiempo de computación corto a pesar de emplear un número         elevado de elementos.
  - La optimización de la ruta es directamente proporcional al tiempo de ejecución para hallarla. Es decir, mientras más óptima se desee     la ruta, más tiempo tardará en ser hallada.
  - La representación gráfica de la solución permite observar que efectivamente  el camino es lógico y coherente.
  - Pueden hallarse diferentes soluciones con diferentes puntos de inicio, pero al final todas señalan el mismo ciclo.
 

# Bibliografia

-   Fuentes Penna, A. (2013) Problema del agente viajero. Recuperado de: https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html
    [Consulta: 1 de mayo de 2019]
-   FreeCodeCamp (Sin fecha) Brute Force Algorithms. Recuperado de: https://guide.freecodecamp.org/algorithms/brute-force-algorithms/
    [Consulta: 1 de mayo de 2019]
-   Lázaro García, J. (Sin fecha) Backtracking. Recuperado de:                                                                               www.cc.uah.es/pub/Alumnos/G_Ing_Informatica/Algoritmia_y_Complejidad/anteriores/Apuntes/08_Backtracking.pdf
    [Consulta: 1 de mayo de 2019]
-   Garg, P. (Sin fecha) Breadth First Search. Recuperado de: 
    https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/ [Consulta: 1 de mayo de 2019]
