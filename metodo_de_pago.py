

class MetodoDePago:
    def __init__(self, tipo, numero, fecha_vencimiento):
        self.tipo = tipo
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento

    
    def validar_informacion(self):
        if self.tipo == "Tarjeta de Crédito":
            if len(self.numero) == 16 and self.numero.isdigit():
                mes, anio = self.fecha_vencimiento.split("/")
                if len(mes) == 2 and len(anio) == 2 and mes.isdigit() and anio.isdigit():
                    return True
        return False
