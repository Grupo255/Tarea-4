# Componente practico Fase 4

# Se importa herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Se mporta para trabajar con fechas (logs)
from datetime import datetime

# LOGS
# Archivo de logs donde se registran errores y eventos guarda todo

# Función que registra mensajes en un archivo de logs
def registrar_log(mensaje):
    # Abre o crea el archivo logs.txt en modo agregar
    with open("logs.txt", "a") as archivo:
        # Escribe fecha + mensaje
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# MANEJO DE ERRORES

# Clase base de errores del sistema
class ErrorSistema(Exception):
    pass 

# Clase específica para errores de validación
class ErrorValidacion(ErrorSistema):
    pass  

# CLASE ABSTRACTA ENTIDAD
# Clase abstracta que represente entidades generales del sistema

class Entidad(ABC):

    # Constructor que recibe ID
    def __init__(self, id):
        self._id = id  # Atributo protegido (encapsulación)

    # Método abstracto 
    @abstractmethod
    def mostrar_info(self):
        pass


# CLASE CLIENTE 
# Clase Cliente con validaciones y encapsulación

class Cliente(Entidad):

    # Se define los datos basicos
    def __init__(self, id, nombre, correo):
        super().__init__(id) 
        self.nombre = nombre 
        self.correo = correo  

    # Se crea un valor al nombre 
    @property
    def nombre(self):
        return self._nombre

    # se guarda nombre con validación 
    @nombre.setter
    def nombre(self, valor):
        # Validación robusta
        if not valor or len(valor) < 3:
            raise ErrorValidacion("Nombre inválido")
        self._nombre = valor

    # se crea un valor al correo
    @property
    def correo(self):
        return self._correo

    # Se guarda el valor del correo con validación 
    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ErrorValidacion("Correo inválido")
        self._correo = valor

    # Implementación del método abstracto
    def mostrar_info(self):
        return f"{self._id} - {self._nombre} - {self._correo}"

# Clase abstracta Servicio
class Servicio(ABC):

    # Constructor del servicio
    def __init__(self, nombre, precio_base):
        self.nombre = nombre  # Nombre del servicio
        self.precio_base = precio_base  # Precio base

    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self, *args):
        pass