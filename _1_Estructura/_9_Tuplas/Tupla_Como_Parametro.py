# Función que recibe una tupla y la desempaqueta
def calcular_area(rectangulo: tuple[int, int]) -> int:
    largo, ancho = rectangulo
    return largo * ancho

def cuadrado(rectangulo: tuple[int, int]) -> tuple[int, int]:
    largo, ancho = rectangulo
    largo = largo * largo
    ancho = ancho * ancho
    return (largo, ancho)

if __name__ == '__main__':
    # Crear la tupla
    dimensiones = (10, 5)

    # Llamar a la función con la tupla
    area = calcular_area(dimensiones)
    print(f"El área del rectángulo es: {area} mts. cuadrados.")

    # Usar la función cuadrado
    largo, ancho = cuadrado(dimensiones)

    # Calcular el nuevo área con los valores modificados
    area2 = largo * ancho
    print(f"El área del nuevo rectángulo es: {area2} mts. cuadrados.")
