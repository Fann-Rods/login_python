#Aqui se coloca toda la interaccióin que va a realizar el usuario con la palicación.
#interface de usuario

from seguridad.usuario import Usuario

class MenuSeguridad:
#Como no hay una funcion no se genera un constructor

    def mostrar_menu(self):
        while(True):
            print("=" * 50)
            print("= Bienvenido al menú de gestión de usuarios =")
            print("1. Iniciar sesion")
            print("2. Registrarse")
            print("0. Salir")
            opcion = int(input("¿Cual es su opción?: "))
            if opcion == 1:
                self.iniciar_sesion()
            elif opcion == 2:
                self.registro()
            elif opcion == 0:
                print("Hasta luego")
                break
    
    def iniciar_sesion(self):
        print("= INICIO DE SESION =")
        correo = input("Ingrese su correo: ")
        clave = input("Ingrese su contraseña: ")

        #Validar usuario y contraseña
        usuario = Usuario(correo, clave)
        estado = usuario.iniciar_sesion()
        #estado = False

        if estado:
            print("Usuario iniciado exitosamente")
            # TODO Entrar a la aplicación de tareas
        else:
            print("Credenciales inválidas. Intente de nuevo")

    def registro(self):
        print("= REGISTRO DE USUARIO =")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        clave = input("Ingrese su contraseña: ") 

        #Guardar en base de datos
        #usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, clave=clave)
        usuario = Usuario(correo, clave, nombre, apellido)
        guardado = usuario.registrar()

        if guardado:
            print("Usuario guardado correctamente")
        else:
            print("Ha ocurrido un error al guardar el usaurio")
    