
def registrar_usuario():
    print("Zona de registro, por favor introduce tus datos:\n")
    usuario = input("Ingrese un usuario: ")
    contrasena = input("Ingrese una contraseña")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    email = input("Ingresa tu email: ")
    telefono = input("Ingresa tu teléfono: ")

    with open("/home/santiago/Documentos/CODERHOUSE/recursos/Base_de_datos.txt", "a") as archivo:
        archivo.write(f"{usuario}|{contrasena}||{nombre}|{apellido}|{email}|{telefono}\n")

    print("Registro finalizado.")

def iniciar_sesion():
    usuario = input("Ingrese su usuario:\n")
    contrasena = input("Ingrese su contraseña:\n")

    with open("/home/santiago/Documentos/CODERHOUSE/recursos/Base_de_datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split("|")
            #nombre = datos[2]
            #apellido = datos[3]
            if datos[0] == usuario and datos[1] == contrasena:
                print(f"Hola {datos[2]} {datos[3]} como estás hoy?\n")
                return
        print("Usuario o contraseña no válidos.")

def menu_principal():
    while True:
        print("")
        print("""Bienvenido a mi Web Playground
         
A continuación debes escoger que deseas hacer: \n""")
        print("r. Registrarse")
        print("i. Iniciar sesión")

        opcion = input("\n")
        if opcion == "r":
            registrar_usuario()
        elif opcion == "i":
            iniciar_sesion()
            break
        else:
            print("Opción inválida. Intenta nuevamente.\n")
menu_principal()

