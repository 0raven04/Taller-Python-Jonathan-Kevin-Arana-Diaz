from math import pow

def suma(lista: list) -> int:
    return sum(lista)

# def potencia(x: int) -> int:
#     return int(pow(x, 2))

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(f"Números originales: {numeros}")

    print(f"La suma total con una función: {suma(numeros)}")

    numerosCuadrados = list(map(lambda x: x * x, numeros))
    print(f"Números cuadrados con una función: {numerosCuadrados}")
