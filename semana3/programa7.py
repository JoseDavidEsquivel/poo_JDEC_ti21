"""
    Programa7
    Nombre: Esquivel Cruz José David
    Fecha: 30/01/2023
    Descripcion: Area y perimetro de un circulo y cuadrado
"""
print("Calculo de Area y Perimetro de un Circulo") # Introduccion al programa, (instrucciones a seguir)
print()
print("Inserte los valores que se piden a continuacion")

radio= int(input("Radio: ")) # Peticion de datos para el calculo de el circulo
perimetrocirculo = 2*3.14159*radio # Operaciones para el calculo de area y perimetro
areacirculo = 3.14159*radio**2

print("El area de un circulo de {} de radio es {}, y su perimetro es de {} ".format(radio,areacirculo,perimetrocirculo)) #     Impresion del Area y Perimetro de un Circulo usando .format

print() # Separacion a la hora de imprimir

print("Calculo de Area y Perimetro de un Cuadrado") # Introduccion al programa, (instrucciones a seguir) 
print()
print("Inserte los valores que se piden a continuacion")

lado= int(input("Medida de un lado: ")) # Peticion de datos para el calculo de el cuadrado
perimetrocuadrado= 4*lado # Operaciones para el calculo de area y perimetro
areacuadrado= lado**2

print("El area de un cuadrado de {} de lado es {}, y su perimetro es de {}".format(lado,areacuadrado,perimetrocuadrado)) # Impresion del Area y Perimetro de un Cuadrado usando .format
