# Ejemplo de recursividad directa
def recursive_sum(arr: list) -> int:
    if len(arr) == 0:
        return 0

    return arr[0] + recursive_sum(arr[1:])


# Ejemplo de recursividad indirecta
def recursive_indirect_sum(arr: list, i: int) -> int:
    if i >= len(arr) - 1:
        return arr[i]
    
    suma = recursive_indirect_sum(arr, i + 1) + arr[i]
    return suma

def recursive_indirect_sum(arr: list) -> int:
    if len(arr) == 0:
        return 0
    
    return recursive_indirect_sum(arr, 0)


def main():
    arr = list(map(int, input()))

    print(recursive_indirect_sum(arr))
    print(recursive_sum(arr))