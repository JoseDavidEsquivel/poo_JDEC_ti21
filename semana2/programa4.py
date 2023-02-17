"""
    Programa4
    Nombre: Esquivel Cruz José David
    Fecha: 24/01/2023
    Descripcion: KEY AND VALUE
"""


numero1 = 10 # Asigna el valor 10 (int) a numero1
numero2 = 5 # Asigna el valor 5 (int) a numero2


print("{} + {} = {} " .format(numero1,numero2,numero1+numero2)) # Codigo fuente del programa3 

"""
print("{} + {} = " .format(numero1,numero2,numero1+numero2)) # Codigo de linea sin una de las llaves (no afecta ni dara error a la hora de ejecutarlo)
"""

print("{n1} + {n2} = {suma}" .format(n1=numero1,n2=numero2,suma=numero1+numero2)) # KEY AND VALUE DE FORMA CORRECTA

print("{n2} + {n2} = {suma}" .format(n1=numero1,n2=numero2,suma=numero1+numero2)) # solo se le ha dado el key de n2 a las llaves y por eso mostrara 5+5=5

"""
print("{n4} + {n4} = {suma}" .format(n1=numero1,n2=numero2,suma=numero1+numero2))
El Key n Value no coincide con lo colodado en el .format
"""

"""
print("{numero1} + {numero2} = {} " .format(numero1,numero2,numero1+numero2)) 
no funciona porque no se le ha asignado la variable para poder ser utilizado por el print
"""
