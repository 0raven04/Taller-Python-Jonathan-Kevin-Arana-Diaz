#Desarrolla un programa en python que utilice
#la POO para registrar un libro (ISBN, TITULO y AUTOR)
#Los atributos debe estar en privado
#debes tener un constructor para el registro
#Debes tener solo getters de cada atributo

#En otra clase deberá registrar una coleccion de libros
#En esta clase debes tener add , delete y  show

# Clase para representar un libro
class Libro:
    def __init__(self, ISBN: int, TITULO: str, AUTOR: str):
        self.__ISBN = ISBN
        self.__TITULO = TITULO
        self.__AUTOR = AUTOR

    # Getters
    def getISBN(self) -> int:
        return self.__ISBN

    def getTITULO(self) -> str:
        return self.__TITULO

    def getAUTOR(self) -> str:
        return self.__AUTOR


# Clase para manejar la colección de libros
class ColeccionLibros:
    def __init__(self):
        self.__libros = []

    def add(self, libro: Libro):
        self.__libros.append(libro)
        print(f"Libro '{libro.getTITULO()}' agregado.")

    def delete(self, ISBN: int):
        for libro in self.__libros:
            if libro.getISBN() == ISBN:
                self.__libros.remove(libro)
                print(f"Libro con ISBN {ISBN} eliminado.")
                return
        print(f"No se encontró un libro con ISBN {ISBN}.")

    def show(self):
            print("\n--- Colección de Libros ---")
            for libro in self.__libros:
                print(f"ISBN: {libro.getISBN()}, Título: {libro.getTITULO()}, Autor: {libro.getAUTOR()}")


# Menú principal con estructura `match`
def menu():

    coleccion = ColeccionLibros()

    while True:
        print("\n--- Biblioteca ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Mostrar colección")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":

                ISBN = int(input("Ingrese el ISBN: "))
                TITULO = input("Ingrese el título: ")
                AUTOR = input("Ingrese el autor: ")
                libro = Libro(ISBN, TITULO, AUTOR)
                coleccion.add(libro)
            case "2":

                (ISBN) = int(input("Ingrese el ISBN del libro a eliminar: "))
                coleccion.delete(ISBN)

            case "3":

                coleccion.show()

            case "4":
                print("Saliendo del sistema.")
                break
            case _:
                print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
