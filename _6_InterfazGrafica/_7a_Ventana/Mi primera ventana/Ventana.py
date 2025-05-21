import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5 import uic
import mariadb

class Ventana(QMainWindow):
    def __init__(self, texto):
        super().__init__()
        uic.loadUi("V1.ui", self)
        self.btnNombre.clicked.connect(self.Imprimir_Mensaje)
        self.texto = texto

    def Imprimir_Mensaje(self):
        self.btnNombre.setText(self.texto)

def conectar_y_consultar():
    try:
        # Establecer conexión a la base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print("Conexión a la base de datos del servidor Ounus")

        # Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuarios"
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Datos en la tabla:")
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre Completo: {fila[1]}, Nombre de Usuario: {fila[2]}, Correo: {fila[3]}, Contraseña: {fila[4]}, Id_Rol: {fila[5]}")

        return "Consulta ejecutada con éxito"

    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return "Error en la consulta"

    finally:
        if cursor:
            cursor.close()
            print("\nConexión cerrada.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    miventanita = Ventana(conectar_y_consultar())
    miventanita.show()
    sys.exit(app.exec_())


