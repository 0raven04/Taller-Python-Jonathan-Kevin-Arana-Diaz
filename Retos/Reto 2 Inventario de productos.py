def menu():
    print("\nInventario Básico")
    print("1. agregar producto")
    print("2. mostrar inventario")
    print("3. vender producto")
    print("4. salir")


def agregar(inventario):
    nombre = input("ingrese el nombre del producto: ")
    cantidad = int(input("ingrese la cantidad: "))

    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print(f"stock actualizado: {nombre} ahora tiene {producto[1]} unidades")
            return

    inventario.append([nombre, cantidad])
    print(f"producto agregado: {nombre} con {cantidad} unidades")


def mostrar_inventario(inventario):
    if not inventario:
        print("el inventario está vacío.")
        return
    print("\ninventario actual:")
    for producto in inventario:
        print(f"{producto[0]}: {producto[1]} unidades")


def venta(inventario):
    nombre = input("ingrese el nombre del producto a vender: ")
    for producto in inventario:
        if producto[0] == nombre:
            cantidad = int(input("ingrese la cantidad a vender: "))
            if cantidad > producto[1]:
                print("no hay suficiente stock disponible")
                return
            producto[1] -= cantidad
            if producto[1] == 0:
                inventario.remove(producto)
                print(f"{nombre} agotado y eliminado del inventario")
            else:
                print(f"venta realizada: {nombre} ahora tiene {producto[1]} unidades")
            return
    print("el producto no está en el inventario")


def main():
    inventario = []
    ejecutando = True
    while ejecutando:
        menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar(inventario)
            case "2":
                mostrar_inventario(inventario)
            case "3":
                venta(inventario)
            case "4":
                print("Saliendo del sistema...")
                ejecutando = False
            case _:
                print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
