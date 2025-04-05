# Lista que almacenara los libros como diccionarios
biblioteca = []

# Diccionario para gestionar los usuarios y sus libros prestados
usuarios = {}

# Funcion para agregar libros
def agregar_libro(titulo, autor, genero, copias=1):
    libro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'copias': copias
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado")

# funcion  para buscar libros
def buscar_libros(titulo=None, autor=None, genero=None):
    for libro in biblioteca:
        if ((titulo and titulo.lower() in libro['titulo'].lower()) or
            (autor and autor.lower() in libro['autor'].lower()) or
            (genero and genero.lower() in libro['genero'].lower())):
            yield libro

# funcion para mostrar libros disponibles
def mostrar_libros_disponibles():
    print("\nLibros disponibles en la biblioteca:")
    for libro in biblioteca:
        if libro['copias'] > 0:
            print(f"{libro['titulo']} | Autor: {libro['autor']} | Genero: {libro['genero']} | Copias: {libro['copias']}")

# Funcion para prestar un libro
def prestar_libro(usuario, titulo):
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower() and libro['copias'] > 0:
            libro['copias'] -= 1
            usuarios.setdefault(usuario, []).append(libro['titulo'])
            print(f"Libro '{libro['titulo']}' prestado a {usuario}")
            return
    print(f"No se pudo prestar el libro '{titulo}' Puede que no haya copias disponibles")

# Funcion para devolver un libro
def devolver_libro(usuario, titulo):
    if usuario in usuarios and titulo in usuarios[usuario]:
        for libro in biblioteca:
            if libro['titulo'].lower() == titulo.lower():
                libro['copias'] += 1
                usuarios[usuario].remove(titulo)
                print(f"{usuario} ha devuelto el libro '{titulo}'")
                return
    print(f"{usuario} no tiene el libro '{titulo}' prestado")

def menu():
    while True:
        print("\n--- Biblioteca Virtual ---")
        print("1. Agregar libro")
        print("2. Buscar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                titulo = input("Titulo: ")
                autor = input("Autor: ")
                genero = input("Genero: ")
                try:
                    copias = int(input("Numero de copias: "))
                except ValueError:
                    copias = 1
                agregar_libro(titulo, autor, genero, copias)

            case "2":
                print("\n--- Buscar libro ---")
                titulo = input("Buscar por titulo (dejar en blanco si no aplica): ")
                autor = input("Buscar por autor (dejar en blanco si no aplica): ")
                genero = input("Buscar por genero (dejar en blanco si no aplica): ")

                resultados = list(buscar_libros(
                    titulo=titulo if titulo else None,
                    autor=autor if autor else None,
                    genero=genero if genero else None
                ))

                if resultados:
                    for libro in resultados:
                        print(f"{libro['titulo']} | {libro['autor']} | {libro['genero']} | Copias: {libro['copias']}")
                else:
                    print("No se encontraron libros")

            case "3":
                usuario = input("Nombre de usuario: ")
                titulo = input("Titulo del libro a prestar: ")
                prestar_libro(usuario, titulo)

            case "4":
                usuario = input("Nombre de usuario: ")
                titulo = input("Titulo del libro a devolver: ")
                devolver_libro(usuario, titulo)

            case "5":
                mostrar_libros_disponibles()

            case "6":
                print("Saliendo del sistema")
                break

            case _:
                print("Opcion no valida, intente nuevamente")

if __name__ == "__main__":
    menu()
