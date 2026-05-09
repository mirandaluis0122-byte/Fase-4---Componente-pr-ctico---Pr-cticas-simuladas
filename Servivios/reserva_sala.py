from modelos.servicio import Servicio
from modelos.excepciones import ServicioError

class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad):
        super().__init__(nombre, tarifa_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        total = self.tarifa_base * horas
        total -= total * descuento

        return total

    def descripcion(self):
        return f"Reserva de sala con capacidad para {self.capacidad} personas"