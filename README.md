# Travelling Salesman Problem (TSP) / Problema del vendedor viajante

El problema del vendedor viajante (TSP por sus siglas en inglés) consiste en resolver la siguiente interrogante: cuál es la ruta
más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?

El problema del vendedor viajante (TSP por sus siglas en inglés) se encuentra clasificado como problema de optimización combinatoria; es decir, un problema donde intervienen cierto número de variables, donde cada una puede tener N diferentes valores y cuyo número de combinaciones es de carácter exponencial. Ello da lugar a múltiples soluciones óptimas (soluciones que se calculan en un tiempo finito) para una instancia.

En el contexto de nuestro problema, utilizamos como ciudades a los centros poblados del Perú.

   [![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)

# Nuestra propuesta
La solución al problema presentado representa un desafío, ya que no emplearemos algoritmos de optimización, sino que nos limitaremos a utilizar algoritmos de búsqueda. En ese sentido, solo es posible solucionar el problema en tiempos de cómputo pequeños cuando utilizamos un número pequeño de elementos. Además, cabe resaltar que consideramos todos los centros poblados conectados entre sí; es decir, existe un camino de un punto hacia cualquier otro.
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
    >Es un algoritmo que consiste en recursión intensiva para resolver problemas por etapas, que utiliza como árbol de decisiones la propia organización de la recursión.Cuando se “avanza” de etapa se realiza una llamada recursiva, y cuando se “retrocede” lo que
se hace es terminar el correspondiente proceso recursivo, con lo que efectivamente se vuelveal estado anterior por la pila de entornos creada en la recursión. 

   [![](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)
   
   
 - BFS:
    >Es un algoritmo que consiste en un recorrido transversal de los elementos (si se visualiza como un árbol). Recorre todos los elementos del mismo nivel, y luego desciende al siguiente nivel y continúa el recorrido de manera transversal.

   [![](https://i.imgur.com/kxETgI0.png)](https://i.imgur.com/kxETgI0.png)

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
# Conclusiones

  - Los algoritmos de búsqueda exhaustiva pueden requerir un tiempo de computación astronómico si emplean un elevado número de               elementos.
  - Los algoritmos de búsqueda pueden hallar la solución correcta para un grupo pequeño de elementos, pero no de la forma más óptima.
 

# Bibliografia

-   Fuentes Penna, A. (2013) Problema del agente viajero. Recuperado de: https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html
    [Consulta: 1 de mayo de 2019]
-   FreeCodeCamp (Sin fecha) Brute Force Algorithms. Recuperado de: https://guide.freecodecamp.org/algorithms/brute-force-algorithms/
    [Consulta: 1 de mayo de 2019]
-   Lázaro García, J. (Sin fecha) Backtracking. Recuperado de:                                                                               www.cc.uah.es/pub/Alumnos/G_Ing_Informatica/Algoritmia_y_Complejidad/anteriores/Apuntes/08_Backtracking.pdf
    [Consulta: 1 de mayo de 2019]
-   Garg, P. (Sin fecha) Breadth First Search. Recuperado de: 
    https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/ [Consulta: 1 de mayo de 2019]
