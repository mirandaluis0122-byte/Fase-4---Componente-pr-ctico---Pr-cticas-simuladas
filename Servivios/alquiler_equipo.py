from modelos.servicio import Servicio
from modelos.excepciones import ServicioError

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, tipo_equipo):
        super().__init__(nombre, tarifa_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias, descuento=0):

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a cero")

        total = self.tarifa_base * dias
        total -= total * descuento

        return total

    def descripcion(self):
        return f"Alquiler de equipo tipo {self.tipo_equipo}"