

class Producto:
    def __init__(self, nombre, precio, descripcion, categoria):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria

# Información del producto
    def obtener_informacion(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\nDescripción: {self.descripcion}\nCategoría: {self.categoria}"

    def __str__(self):
        return self.nombre
    