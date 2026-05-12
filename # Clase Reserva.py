# Clase Reserva
class Reserva:

    # Constructor de la reserva
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente  # Objeto cliente
        self.servicio = servicio  # Objeto servicio
        self.duracion = duracion  # cantidad, unidad
        self.estado = "pendiente"  # Estado inicial

    # Método para confirmar la reserva
    def confirmar(self):

        try:
            # Separa cantidad y unidad
            cantidad, unidad = self.duracion

            # Valida que la cantidad sea positiva
            if cantidad <= 0:
                raise ErrorValidacion("Duración inválida")

            # Convierte unidad a minúscula
            unidad = unidad.lower()

            # Si el servicio es de tipo equipo
            if isinstance(self.servicio, ServicioEquipo):

                # Conversión a días
                if unidad in ["dia", "dias"]:
                    dias = cantidad
                elif unidad in ["hora", "horas"]:
                    dias = cantidad / 24
                elif unidad in ["minuto", "minutos"]:
                    dias = cantidad / (24 * 60)
                else:
                    raise ErrorValidacion("Unidad inválida para este servicio")

                # Calcula costo
                costo = self.servicio.calcular_costo(dias)

            else:
                # Conversión a horas
                if unidad in ["hora", "horas"]:
                    horas = cantidad
                elif unidad in ["minuto", "minutos"]:
                    horas = cantidad / 60
                elif unidad in ["dia", "dias"]:
                    horas = cantidad * 24
                else:
                    raise ErrorValidacion("Unidad inválida para este servicio")

                # Calcula costo
                costo = self.servicio.calcular_costo(horas)

            # Cambia estado a confirmada
            self.estado = "confirmada"

            # Muestra costo redondeado
            print(f"Reserva confirmada. Costo: {round(costo,2)}")

        except Exception as e:
            # Registra error en logs
            registrar_log(e)

            # Cambia estado a error
            self.estado = "error"

            # Muestra mensaje
            print(f"Error en la reserva: {e}")

    # Método para mostrar información de la reserva
    def mostrar(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre} - {self.estado}"