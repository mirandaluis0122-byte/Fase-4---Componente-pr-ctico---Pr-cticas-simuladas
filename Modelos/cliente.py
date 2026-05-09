from modelos.entidad import Entidad
from modelos.excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteError("El nombre del cliente es inválido")

        if "@" not in self.__correo:
            raise ClienteError("Correo electrónico inválido")

        if not self.__telefono.isdigit():
            raise ClienteError("El teléfono debe contener solo números")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"