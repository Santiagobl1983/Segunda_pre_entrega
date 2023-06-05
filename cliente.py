

class Cliente:
    def __init__(self,usuario,contrasena,nombre,apellido,telefono,e_mail):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.e_maile_mail = e_mail
        self.sesion_iniciada = False
        self.carrito = []

# Registro en el sistema
    def __registrar(self):
        print("Registrando al usuario:", self.nombre)

# Inicio de sesión
    def __iniciar_sesion(self):
        print("Iniciando sesión:", self.nombre)
        self.sesion_iniciada = True

# Explorar la tienda de productos
    def explorar_tienda(self):
        if self.sesion_iniciada:
            print("Explorando la tienda de productos")
        else:
            print("Debes iniciar sesión para explorar la tienda")

# Agregar un producto al carrito de compras
    def agregar_al_carrito(self, producto):
        if self.sesion_iniciada:
            self.carrito.append(producto)
            print("Producto", producto, "agregado al carrito")
        else:
            print("Debes iniciar sesión para agregar productos al carrito")

# Mostrar el contenido del carrito de compras
    def ver_carrito(self):
        if self.sesion_iniciada:
            print("Carrito de compras:")
            for producto in self.carrito:
                print("-", producto)
        else:
            print("Debes iniciar sesión para ver el carrito")

# Compra de los productos del carrito
    def __comprar (self):
        if self.sesion_iniciada:
            if self.carrito:
                print("Procesando compra:")
                for producto in self.carrito:
                    print("Comprando producto:", producto)
                print("¡Compra realizada!")
                self.carrito.clear()
            else:
                print("El carrito de compras está vacío")
        else:
            print("Debes iniciar sesión para realizar una compra")

