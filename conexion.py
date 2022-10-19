import mysql.connector

def conectar():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="physioDeveloper_task_python",
            port=3308
        )
        print("Se ha conectado a la aplicación")

        return db #(retornar un db si hay conexión ala base de datos)
    except Exception as ex:
        print("Error al conectarse a la base de datos", ex)