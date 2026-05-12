# Clase ServicioSala 
class ServicioSala(Servicio):

    # Calcula costo por horas con recargo del 10%
    def calcular_costo(self, horas=1):
        return self.precio_base * horas * 1.1


# Clase ServicioEquipo 
class ServicioEquipo(Servicio):

    # Calcula costo por días con descuento del 5%
    def calcular_costo(self, dias=1):
        return self.precio_base * dias * 0.95


# Clase ServicioAsesoria
class ServicioAsesoria(Servicio):

    # Calcula costo por horas con recargo del 20%
    def calcular_costo(self, horas=1):
        return self.precio_base * horas * 1.2
    #Marly Cabezas 