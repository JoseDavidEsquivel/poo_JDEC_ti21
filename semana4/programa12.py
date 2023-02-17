"""
    Programa12
    Nombre: Esquivel Cruz José David
    Fecha: 09/02/2023
    Descripcion: definicion de funciones (con typing)(solo disponible para versiones posteriores a 3.9 de python)
"""

def mayor(numero1:int,numero2:int) ->int | None: # Definicion de la funcion llamada "mayor" con la diferencia de que aqui se le esta dando el tipeo de variable entera (int)
    result = None
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