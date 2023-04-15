# Problema #1 CR

# Mi compa el gym rat.
Bruno es un tremendo gym rat de los grandes, tan grande que para todas las comidas que podría tener en el día, tiene contabilizado la cantidad de proteínas que pierde o gana por cada comida. Bruno tiene un problemon, una vez que empieza no puede saltarse comidas, por que su mamá le pega si no se come todo lo que le va sirviendo, pero si puede detenerse en donde quiera diciéndole "jefa, ya me llené".
Por lo que quiere encontrar por cada conjunto de comidas la mayor cantidad de proteínas que pueda ganar. Para esto, Bruno te da $N$ listas de $T$ enteros, de las cuales debes de encontrar la suma de un subconjunto con $n$ comidas tal que la suma de esas $n$ comidas sea lo más grande posible.
## Entradas:
Donde $N$ es el número de casos, lo que sería el número de arreglos que Bruno te da, y $T$ el número de elementos por cada arreglo desde 1 hasta N.
## Salidas:
Deberas imprimir $N$ veces la suma más grande de los subconjuntos consecutivos en cada arreglo de $T$ elementos.
## Ejemplos:
|Entrada|Salida|Descripcion|
| ------- | ------- | ------- |
| 4 <br> 1 -100 5 -1 4 -20 <br> 67 -89 1 5 4 <br> -100 12 43 -10 13 0 -89 <br> -100 -5 -6 -8 1 2 3 -80 20 | <br> Caso #1: 8 <br> Caso #2: 67 <br> Caso #3: 58 <br> Caso #4: 20| Número de listas de entrada. <br> 5 - 1 + 4 = 8 <br> El 67 por sí solo es mayor que la suma de los tres últimos números positivos. <br> 12 + 43 - 10 + 13 = 58 <br> Lo mismo que en el caso #2, pero ahora colocado en el extremo opuesto. |

## Límites:
$ 1 \leq N \leq 5 $

$ 5 \leq T \leq 15 $
