import json
import sys


def ciclo():
    with open("archivos Json/RFC.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)  # Carga el contenido del archivo JSON

    for persona in datos["personas"]:
        yield persona


def mayor_de_edad(nombre: str, edad: int):
    if edad >= 18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")


if __name__ == '__main__':


    # Definición de códigos ANSI
    RESET = "\033[0m"  # Restablece el color a su valor por defecto
    # Colores de texto
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Colores de fondo
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Version corta de abrir un archivo Json
    # Abre el archivo JSON en modo de lectira u with se ecnarga de cerrar

    # Iterar sobre las personas usando el generador
    i = 1
    for persona in ciclo():  # Se recibe el diccionario completo

        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(YELLOW)
            case 4:
                sys.stdout.write(BLUE)
            case 5:
                sys.stdout.write(MAGENTA)
            case _:
                sys.stdout.write(RESET)

        print("----------------------------")
        print(f"id: {persona['id']}")
        print(f"nombre: {persona['nombre']}")
        print(f"edad: {persona['edad']}")
        print(f"rfc: {persona['rfc']}")
        mayor_de_edad(persona["nombre"], persona["edad"])
        print("----------------------------")  # Linea en blacno para separa
        i += 1


