from modelos.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):

        try:
            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as error:
            raise ReservaError("Error al procesar la reserva") from error

        else:
            self.confirmar()
            return costo

        finally:
            print("Proceso de reserva finalizado")