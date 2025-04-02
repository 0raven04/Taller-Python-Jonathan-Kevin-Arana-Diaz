import json
import sys

# Definición de códigos ANSI
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"

# Generador que extrae información del archivo JSON con manejo de excepciones
def ciclo():
    try:
        with open("archivos Json/RFC.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)  # Carga el contenido del archivo JSON

        for persona in datos["personas"]:
            yield persona

    except FileNotFoundError:
        sys.stdout.write(RED)
        print("No existe el archivo 'archivos Json/RFC.json'")
        sys.stdout.write(RESET)
    except json.JSONDecodeError:
        sys.stdout.write(RED)
        print("El archivo no contiene un JSON válido")
        sys.stdout.write(RESET)
    except Exception as e:
        sys.stdout.write(GREEN)
        print(f"Pues no sé qué ocurrió jsjsjsjsjs: ", e )
        sys.stdout.write(RESET)
    finally:
        #Cierra el archivo manualmente
        archivo.close()
        print("archivo Json cerrado")
        sys.stdout.write(RESET)

# Función que determina si una persona es mayor o menor de edad y cambia el color de la salida
def mayor_de_edad(nombre: str, edad: int):
    if edad >= 18:
        sys.stdout.write(GREEN)
        print(f"{nombre} es mayor de edad")
    else:
        sys.stdout.write(RED)
        print(f"{nombre} es menor de edad")

    sys.stdout.write(RESET)  # Restablecer el color después de imprimir

if __name__ == '__main__':
    # Iterar sobre las personas usando el generador
    for persona in ciclo():
        if isinstance(persona, dict):  # Solo imprimir si 'persona' es un diccionario válido
            print("----------------------------")
            print(f"id: {persona['id']}")
            print(f"nombre: {persona['nombre']}")
            print(f"edad: {persona['edad']}")
            print(f"rfc: {persona['rfc']}")
            mayor_de_edad(persona["nombre"], persona["edad"])
            print("----------------------------")  # Línea en blanco para separar
