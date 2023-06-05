from cliente import Cliente
from producto import Producto

class Pedido(Cliente,Producto):
    def __init__(self, Cliente,Producto):
        self.Cliente = Cliente
        self.Producto = Producto
        self.carrito = []

    def agregar_producto(self, Producto):
        self.Producto.append(Producto)

    def calcular_total(self):
        total = 0
        for producto in self.Producto:
            total += Producto.precio
        return total
    
    def __str__(self):
        return f"Pedido del cliente: {self.Cliente}"