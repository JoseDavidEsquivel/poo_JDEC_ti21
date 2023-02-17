"""
    Programa9
    Nombre: Esquivel Cruz José David
    Fecha: 30/01/2023
    Descripcion: Programa que imprima numero mayor o none si son iguales (Ulitizacion de Unit Test)
"""

numero1= int(input("Inserte el primer valor : ")) # Solicitud de los valores en enteros
numero2= int(input("Inserte el segundo valor : ")) # Solicitud de los valores en enteros

if numero1>numero2: # If para la comparacion de los dos numeros antes dados 
    print(numero1) # Accion si se cumple el IF
elif numero2>numero1: # 2da condicion de comparacion
    print(numero2) # Accion si se cumple el elif #1
elif numero1==numero2: # 3ra condicion de comparacion para estos valores (Utilizacion del valor "None")
    print(None) # Accion si se cumple el elif #2
    