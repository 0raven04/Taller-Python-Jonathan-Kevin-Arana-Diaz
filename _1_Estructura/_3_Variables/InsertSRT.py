if __name__ == '__main__':
    palabra: str = "%s"
    lista: list = ["nombre", "apellido_paterno", "nombre_usuario", "edad", "correo_electronico", "contraseña"]

    t = len(lista)
    print(t)

    palabra_lista = ["%s"] * len(lista)

    campos = ",".join(lista)
    camposP = ",".join(palabra_lista)

    querySQL = f"INSERT INTO tabla({campos}) VALUES ({camposP})"
    print(querySQL)
