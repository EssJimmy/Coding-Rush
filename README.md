# Los tacos de canasta
Jimmy y su buen compa el Canguro Barrera tienen un buen de hambre después de haberse rifado estudiando OpAmps 10 minutos antes del examen de electrónica, por lo que deciden irse por unos legendarios tacos de canasta afuera del ITAM. Como buen chilango, Barrera pensó que aceptaban tarjeta de crédito y a Jimmy por ser de pueblo, no sabe usar un cajero automático, por lo que los dos deciden juntar la cantidad de dinero que tienen para ver si se pueden comprar un taco cada uno. Los precios varian según el tipo de taco, por lo que quieren ver para qué tacos les convienen más para que se acaben todo su dinero.

Si logran juntar 15 pesos, y los precios son [3, 6, 2, 7, 8, 10, 25, 14], les conviene comprarse un taco de 7 pesos y uno de 8 pesos. Considera que para este problema, siempre existirá una solución única.

## Entradas
* $1 \leq t \leq 50$ - La cantidad de veces que deberas correr tu solución
* $2 \leq m \leq 10^4$ - El dinero que juntaron Jimmy y Barrera
* $2 \leq n \leq 10^4$ - La cantidad de tacos disponibles en el menú
* $1 \leq cost[i] \leq 10^4$ - Cuanto cuesta cada taco separado por un espacio

## Salida
* $int[2]$ - Una lista de tamaño dos que contenga las posiciones de los tacos que se comprarán, en orden ascendente.

## Ejemplos y pruebas

```
Entrada     Salida
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
```