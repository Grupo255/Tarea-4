# Lista para almacenar clientes
clientes = []

# Lista para almacenar reservas
reservas = []

# Lista de servicios disponibles
servicios = [
    ServicioSala("Sala", 100),
    ServicioEquipo("Equipo", 50),
    ServicioAsesoria("Asesoria", 80)
]


# Función del menú principal
def menu():

    # Bucle infinito hasta salir
    while True:

        # Mostrar opciones
        print("\n--- SISTEMA SOFTWARE FJ ---")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Crear reserva")
        print("4. Ver reservas")
        print("5. Salir")

        # Leer opción del usuario
        opcion = input("Seleccione: ")

        try:

            # Registrar cliente
            if opcion == "1":
                nombre = input("Nombre: ")
                correo = input("Correo: ")

                cliente = Cliente(len(clientes)+1, nombre, correo)
                clientes.append(cliente)

                print("Cliente registrado")

            # Mostrar clientes
            elif opcion == "2":
                for c in clientes:
                    print(c.mostrar_info())

            # Crear reserva
            elif opcion == "3":

                if not clientes:
                    print("No hay clientes")
                    continue

                print("Clientes:")
                for c in clientes:
                    print(c.mostrar_info())

                try:
                    id_cliente = int(input("Seleccione ID cliente: "))
                    cliente = clientes[id_cliente - 1]
                except:
                    raise ErrorValidacion("Cliente inválido")

                print("Servicios:")
                for i, s in enumerate(servicios):
                    print(i, s.nombre)

                try:
                    id_servicio = int(input("Seleccione servicio: "))
                    servicio = servicios[id_servicio]
                except:
                    raise ErrorValidacion("Servicio inválido")

                entrada = input("Duración (ej: 2 horas): ").strip().lower()

                try:
                    cantidad_str, unidad = entrada.split(maxsplit=1)
                    cantidad = int(cantidad_str)
                except:
                    raise ErrorValidacion("Formato inválido. Ej: 2 horas")

                unidad = unidad.replace(".", "").replace(",", "")

                reserva = Reserva(cliente, servicio, (cantidad, unidad))
                reserva.confirmar()
                reservas.append(reserva)

            # Mostrar reservas
            elif opcion == "4":
                for r in reservas:
                    print(r.mostrar())

            # Salir
            elif opcion == "5":
                print("Saliendo...")
                break

            # Opción inválida
            else:
                print("Opción inválida")

        except Exception as e:
            registrar_log(e)
            print(f"Error en operación: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()