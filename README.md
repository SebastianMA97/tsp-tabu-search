# Tabu Search para el Problema del Viajante (TSP)
Proyecto académico que implementa el algoritmo de **Tabu Search** para resolver el
**Problema del Viajante (Traveling Salesman Problem, TSP)**.
El objetivo es encontrar un recorrido de costo mínimo que visite todas las ciudades
exactamente una vez y regrese al punto de inicio.

## Descripción
El algoritmo parte de una solución inicial aleatoria y explora su vecindad aplicando
movimientos de inversión de subrutas.
Para evitar ciclos y estancamiento en óptimos locales, se utiliza una **lista tabú**
que prohíbe temporalmente ciertos movimientos recientes.

El proceso se repite durante un número fijo de iteraciones, manteniendo el mejor
recorrido encontrado.
