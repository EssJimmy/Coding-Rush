# este problema consiste en contar el numero de promedios unicos
# entre el valor maximo y minimo de un arreglo
# cada que hacemos un promedio, deberemos quitar los dos numeros
# de los que tomamos el promedio para no repetirlos
def solve(n:int, arr:list):
    s = set() # creamos nuestro set
    arr.sort() # ordenamos el arreglo para hacer mas facil el recorrer el arreglo
    # asi podemos tomar un indice al principio y al final

    for i in range(n//2):
        s.add((arr[i] + arr[n - i - 1])/2) # añadimos el promedio al set, si es unico se añadira

    print(len(s)) # la respuesta correcta es el tamaño de nuestro set

def main():
    n = int(input()) # tamaño del arreglo
    arr = list(map(int, input().split())) # arreglo

    solve(n, arr) # llamada a la funcion

if __name__ == '__main__':
    main()