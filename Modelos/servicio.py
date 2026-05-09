from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass