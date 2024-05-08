def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0: # caso base, evita que la funcion corra infinitamente
        return
    
    hanoi(n - 1, from_rod, aux_rod, to_rod) # cambiamos el disco n-1 de la torre A a la torre B
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}") # imprimimos los cambios
    hanoi(n - 1, aux_rod, to_rod, from_rod) # cambiamos el disco n-1 de la torre B a la torre C


def main():
    n = 3
    hanoi(n, 'A', 'C', 'B')


if __name__ == "__main__":
    main()