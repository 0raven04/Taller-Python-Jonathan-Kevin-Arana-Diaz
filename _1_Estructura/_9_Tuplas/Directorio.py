if __name__ == '__main__':
    # Crear el diccionario con datos incluyendo el RFC
    agenda = {}

    agenda["GOAT800717"] = ("GOAT800717", "Tomás Gonzalez", "csctomasgonzalez@gmail.com", "2228567")
    agenda["GOAT800719"] = ("GOAT800719", "Luis Gonzalez", "luis85@gmail.com", "2228123")
    agenda["GOAT800718"] = ("GOAT800718", "Fabiola Gonzalez", "fabis25@gmail.com", "2228234")
    agenda["GOAT800710"] = ("GOAT800710", "Fernando Gonzalez", "fergon56@gmail.com", "3455678")

    # Desempaquetar los valores incluyendo el RFC
    rfc, nombre, correo, numero = agenda["GOAT800717"]

    # Imprimir los resultados incluyendo el RFC
    print(f"RFC: {rfc}\nNombre: {nombre}\nCorreo: {correo}\nNúmero: {numero}")
