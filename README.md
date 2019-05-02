# Travelling Salesman Problem (TSP) / Problema del vendedor viajante

El problema del vendedor viajante (TSP por sus siglas en inglés) consiste en resolver la siguiente interrogante: cuál es la ruta
más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?

El problema del vendedor viajante (TSP por sus siglas en inglés) se encuentra clasificado como problema de optimización combinatoria; es decir, un problema donde intervienen cierto número de variables, donde cada una puede tener N diferentes valores y cuyo número de combinaciones es de carácter exponencial. Ello da lugar a múltiples soluciones óptimas (soluciones que se calculan en un tiempo finito) para una instancia.

   [![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AntColony.gif/800px-AntColony.gif)

# Nuestra propuesta
La solución al problema presentado representa un desafío, ya que no emplearemos algoritmos de optimización, sino que nos limitaremos a utilizar algoritmos de búsqueda. En ese sentido, solo es posible solucionar el problema en tiempos de cómputo pequeños cuando utilizamos un número pequeño de elementos.
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
    >Es un algoritmo

   [![](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)](https://static.javatpoint.com/tutorial/daa/images/backtracking-introduction.png)

# Complejidad de las estrategias

- Complejidad Solucion 1: (Backtracking)
    ```sh
    $ cd dillinger
    $ npm install -d
    $ node app
    ```
- Complejidad Solucion 2: (BFS)
    ```
    rangoCambio=Arreglo[1:] #solo nos interesa los elementos que no son el punt ode inicio
   perm = permutations(rangoCambio) #n-1!
   for i in perm: #recorre todas las permutaciones creadas
   esta = bfs([Arreglo[0]]+list(i),0)
   if(solMenor>=esta[1]):
	solMenor=esta[1]
	ordenSol=esta[0]
   ```

# Conclusiones

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

# Bibliografia

-   Fuentes Penna, A. (2013) Problema del agente viajero. Recuperado de: https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html
    [Consulta: 1 de mayo de 2019]
-   FreeCodeCamp (Sin fecha) Brute Force Algorithms. Recuperado de: https://guide.freecodecamp.org/algorithms/brute-force-algorithms/
    [Consulta: 1 de mayo de 2019]
-   Lázaro García, J. (Sin fecha) Backtracking. Recuperado de:                                                                               www.cc.uah.es/pub/Alumnos/G_Ing_Informatica/Algoritmia_y_Complejidad/anteriores/Apuntes/08_Backtracking.pdf
    [Consulta: 1 de mayo de 2019]
 
