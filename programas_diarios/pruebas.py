class Alumno:

    __nombre = None #Esta variable se vuelve privada con "__"
    __matricula = None
    __carrera = None

    def __init__(self):
        print("Carrera")

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setCarrera(self, carrera):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera

luis = Alumno()
luis.setNombre("Luis")
print(luis.getNombre())

luis.setMatricula("1722114500")
print(luis.getMatricula())

luis.setCarrera("Terapia Fisica")
print(luis.getCarrera())