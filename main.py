from cliente import Cliente
from producto import Producto
from tienda import Tienda
from pedido import Pedido
from metodo_de_pago import MetodoDePago


# Instanciando un cliente
cliente1 = Cliente("sbl","1234","Santiago","Barberan","099345223","sbl@gmail.com")
# Registro de cliente
cliente1.registrar()
# Iniciar sesión del cliente
cliente1.iniciar_sesion()
# Explorar la tienda de productos
cliente1.explorar_tienda()
# Agregar productos al carrito
cliente1.agregar_al_carrito("x producto")
# Ver el contenido del carrito
cliente1.ver_carrito()
# Realizar la compra
cliente1.comprar()
# Ver el contenido del carrito después de la compra
cliente1.ver_carrito()


# Instanciando un producto
producto1 = Producto("antena", 150, "antena de WI-FI","Tecnología")


# Instanciando una tienda
tienda1 = Tienda()
# Agregar productos a la tienda
tienda1.agregar_producto(producto1)
# Buscar productos por categoría en la tienda
productos_electrónicos = tienda1.buscar_productos_por_categoria("Tecnología")
for producto in productos_electrónicos:
    print(producto.obtener_informacion())
    print("--------------------")


# Instanciar un pedido para un cliente
pedido = Pedido("Santiago Barberán")
# Agregar productos al pedido
pedido.agregar_producto(producto1)
# Calcular el total del pedido
total = pedido.calcular_total()
print("Total del pedido:", total)



# Instanciando la clase MetodoDePago
metodo_pago = MetodoDePago("Tarjeta de Crédito", "1234 5678 9012 3456", "12/27")
# Validando información del método de pago
if metodo_pago.validar_informacion():
    print("La información del método de pago es válida")
else:
    print("La información del método de pago no es válida")

