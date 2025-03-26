import json

if __name__ == '__main__':
    #Version corta de abrir un archivo Json
    #Abre el archivo JSON en modo de lectira u with se ecnarga de cerrar
    with open("Datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) #Carga el contenido del archivo JSON

    #Muestra el contenido del JSON
    for persona in datos["personas"]:
        print("----------------------------")
        print("Nombre: ", persona["nombre"])
        print("Edad: ", persona["edad"])
        print("Ciudad: ", persona["Ciudad"])
        print("Estado: ", persona["estado"])
        print("----------------------------")#Linea en blacno para separa