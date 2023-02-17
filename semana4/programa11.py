"""
    Programa11
    Nombre: Esquivel Cruz José David
    Fecha: 09/02/2023
    Descripcion: definicion de funciones
"""

def mayor(numero1,numero2): # Definicion de la funcion llamada "mayor"
    result = None # La asignacion de valor "None" a la variable "result"
    if numero1 > numero2: # if con la condicion de "si numero1 es mayor a numero2"
        result = numero1 # asignacion de la variable "numero1" como "result"
    elif numero2 > numero1: # elif con la condicion de "si numero2 es mayor a numero1"
        result = numero2 # asignacion de la variable "numero2" como "result"
    return result # funcion que permite que retorne la variable result

print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #None
print(mayor(-1,1)) #1
print(mayor(1,-1)) #1
print(mayor(-3,-2)) #-2
print(mayor(1,-2)) #1
print(mayor(-2,1)) #1
    