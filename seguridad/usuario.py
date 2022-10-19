from conexion import conectar
from datetime import date
from hashlib import sha256

class Usuario:

    def __init__(self, correo, clave, nombre=None, apellido=None, id=None, fecha=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__passw = clave
        self.__fecha = fecha

    def registrar(self) -> bool:
        # 1. Conectar a base de datos
        db = conectar()
        if db == None:
            raise Exception("No se encuentra conectado a la base de datos")

        # 2. Crear cursor para los comandos SQL
        cursor = db.cursor()

        # 3. Ejecutar la sentencia sql
        if self.__fecha == None:
            self.__fecha = date.today()

        encriptador = sha256()
        encriptador.update(self.__passw.encode('utf8')) #$%é

        cursor.execute(f"INSERT INTO usuario (nombre, apellido, correo, passw, fecha) values ('{self.__nombre}', '{self.__apellido}', '{self.__correo}', '{encriptador.hexdigest()}', '{self.__fecha}')")
        
        db.commit()
        filas_insertadas = cursor.rowcount
        db.close()

        return filas_insertadas == 1

    def iniciar_sesion(self) -> bool:
        # Conectar a base de datos
        db = conectar()
        if db == None:
            raise Exception("No se encuentra conectado a la base de datos")

        # Abrir un cursor
        cursor = db.cursor()

        # Ejecutar sentencia SQL
        encriptador = sha256()
        encriptador.update(self.__passw.encode('utf8'))

        cursor.execute(f"SELECT * FROM usuario WHERE correo = '{self.__correo}' and passw = '{encriptador.hexdigest()}'")
        
        registros = cursor.fetchall()
        print(registros)
        existe = len(registros) == 1
        
        # Cerrar
        db.close()

        return existe
