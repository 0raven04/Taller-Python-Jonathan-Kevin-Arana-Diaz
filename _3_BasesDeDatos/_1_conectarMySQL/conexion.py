import mariadb

def conectar_y_consultar():
    try:
        #Establecer conexión a la base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306#Puerto predeterminado de MariaDB
        )
        print(type(conexion))
        print("Conexión a la base de datos del servidor Ounus")

        #Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from usuarios"
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            print("_________________________________________________________")
            print(f"ID: {fila[0]},\nNombre Completo: {fila[1]},\nNombre de Usuario: {fila[2]},\nCorreo: {fila[3]},\nContraseña:{fila[4]},\nId_Rol: {fila[5]}")
            print("\n")
            print("\n")

        # Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from roles_permisos"
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"id_rol: {fila[0]},\nid_privilegio: {fila[1]},\nfecha_asignacion: {fila[2]}")



        # Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from roles"
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            print("_________________________________________________________")
            print(f"nombre_rol: {fila[0]}")


        # Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from privilegios "
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"titulo_privilegio: {fila[0]}")


    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        # Cerrar la conexi+on y el cursor si están abiertos
            if 'cursor' in locals() and cursor:
                cursor.close()
                print("\nConexion cerrada.")

if __name__ == '__main__':

    conectar_y_consultar()
