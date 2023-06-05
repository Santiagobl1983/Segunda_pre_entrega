

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_productos_por_categoria(self, categoria):
        productos_en_categoria = []
        for producto in self.productos:
            if producto.categoria == categoria:
                productos_en_categoria.append(producto)
        return productos_en_categoria

    def __str__(self):
        return f"Tienda con {len(self.productos)} productos"
