"""
    ProgramaVS
    Nombre: Esquivel Cruz José David
    Fecha: 16/02/2023
    Descripcion: Importacion de clases de un archivo a otro a base de carpetas
"""

class Persona: # Creacion de la clase "Persona"

    __nombre = None # Asignacion de un valor "None" a una variable privada "__nombre" 

    def __init__(self) -> None: # Constructor de la clase Persona
        print("Constructor Persona") # Imprime el texto "Constructor Persona"

    def setNombre(self, nombre:str) -> None: # Metodo para modificar el valor de la variable
        self.__nombre = nombre # Asigna el valor de nombre a la variable privada __nombre

    def getNombre(self) -> str: # Metodo para regresar el valor de la variable privada
        return self.__nombre # Regresa el valor de la variable privada __nombre