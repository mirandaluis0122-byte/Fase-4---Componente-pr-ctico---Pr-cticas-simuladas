from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.excepciones import *

from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

from utilidades.logger import registrar_log


clientes = []
reservas = []


def ejecutar_operaciones():

    operaciones = [

        # Operaciones válidas
        lambda: Cliente("Luis", "luis@gmail.com", "3001234567"),
        lambda: Cliente("Ana", "ana@gmail.com", "3019876543"),

        # Operaciones inválidas
        lambda: Cliente("Li", "correo_invalido", "abc123"),

        # Servicios válidos
        lambda: ReservaSala("Sala VIP", 50000, 20),
        lambda: AlquilerEquipo("Portátiles", 30000, "Computadores"),
        lambda: Asesoria("Asesoría Python", 80000, "Programación"),

        # Servicio inválido
        lambda: ReservaSala("Sala Error", 40000, 10).calcular_costo(-5),

        # Reservas válidas
        lambda: Reserva(
            Cliente("Carlos", "carlos@gmail.com", "3111111111"),
            ReservaSala("Sala Premium", 60000, 30),
            5
        ),

        # Reserva inválida
        lambda: Reserva(
            Cliente("Pedro", "pedro@gmail.com", "3222222222"),
            Asesoria("IA", 100000, "Inteligencia Artificial"),
            -3
        ),

        # Reserva con error interno
        lambda: Reserva(
            Cliente("María", "maria@gmail.com", "3333333333"),
            AlquilerEquipo("Cámaras", 20000, "Video"),
            0
        )
    ]


    for i, operacion in enumerate(operaciones, start=1):

        try:

            resultado = operacion()

            if isinstance(resultado, Cliente):
                clientes.append(resultado)
                print(resultado.mostrar_info())

            elif isinstance(resultado, Reserva):

                costo = resultado.procesar_reserva()
                reservas.append(resultado)

                print(
                    f"Reserva confirmada para {resultado.cliente.nombre}"
                )

                print(f"Costo total: ${costo}")

            else:
                print("Operación ejecutada correctamente")

            registrar_log(f"Operación {i} ejecutada correctamente")

        except Exception as e:

            print(f"Error en operación {i}: {e}")

            registrar_log(
                f"ERROR en operación {i}: {str(e)}"
            )


if __name__ == "__main__":

    try:

        ejecutar_operaciones()

    except Exception as error_general:

        registrar_log(
            f"ERROR GENERAL DEL SISTEMA: {error_general}"
        )

    finally:

        print("\nSistema finalizado correctamente")