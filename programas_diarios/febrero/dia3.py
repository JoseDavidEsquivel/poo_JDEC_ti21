"""
    Programa Dia 3 de Febrero
    Nombre: Esquivel Cruz José David
    Fecha: 3/02/2023
    Descripcion: Hacer una calculadora que solo opere el numero 1 dos veces (MUY UTIL!!!!!!!!)
"""

print("-----------------------------------------------------------------------")
print("BIENVENIDO A LA CALCULADORA QUE SOLO OPERA EL 1")
print("-----------------------------------------------------------------------")
print("Segun la operacion que quieras selecciona el numero")
print("0.- Sumar")
print("1.- Restar")
print("2.- Dividir")
print("3.- Multiplicar")
print("4.- Potencia")
print("5.- Imprimir el 1")
print("6.- bro...")

selector = int(input("")) # DEPENDIENDO DE EL VALOR SE VA A SELECCIONAR VA A SER LA OPERACION A HACER
numero1 = 1
numero2 = 1

if selector == 0:
    print("El resultado de tu operacion es igual a {}" .format(numero1+numero2))
elif selector == 1:
    print("El resultado de tu operacion es igual a {}" .format(numero1-numero2))
elif selector == 2:
    print("El resultado de tu operacion es igual a {}" .format(numero1/numero2))
elif selector == 3:
    print("El resultado de tu operacion es igual a {}" .format(numero1*numero2))
elif selector == 4:
    print("El resultado de tu operacion es igual a {}" .format(numero1**numero2))
elif selector == 5:
    print("GENIAL IMPRIMISTE EL 1")
elif selector > 5:
    print("¿porque?")
elif selector < 0:
    print("¿como es que entra en tu cerebro poner un numero negativo, amigo es solo un valor entre 0 y 5 no es tan dificil")
