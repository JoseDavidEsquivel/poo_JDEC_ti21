from persona import Persona # Importa clases a otros archivos

class Alumno(Persona): # Creacion de la clase Alumno

    def __init__(self)-> None: # Constructor de la clase Alumno
        super().__init__() # Llama al constructo de la clase Persona
        print("Constructor Alumno") # Muestra el mensaje "Construcroe Alumno"

objeto_alumno = Alumno() # Crea un objeto de la clase Alumno e invoca al constructor
objeto_alumno.setNombre ("Dejah") # Llama al metodo setNombre de la clase Persona y le pasa el parametro "Dejah"
print(objeto_alumno.getNombre()) # Llama al metodo getNombre e imprime el valor del nombre