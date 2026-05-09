from modelos.servicio import Servicio
from modelos.excepciones import ServicioError

class Asesoria(Servicio):

    def __init__(self, nombre, tarifa_base, especialidad):
        super().__init__(nombre, tarifa_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        impuesto = 0.19

        total = self.tarifa_base * horas
        total += total * impuesto
        total -= total * descuento

        return total

    def descripcion(self):
        return f"Asesoría especializada en {self.especialidad}"
    