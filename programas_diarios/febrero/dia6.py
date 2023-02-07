"""
    Programa Dia 6 de Febrero
    Nombre: Esquivel Cruz José David
    Fecha: 6/02/2023
    Descripcion: Inserte Contraseña
"""

print("")
print("-----------------------------------------------------------------------")
print("|              Creacion y Verificacion de una Contraseña              |")
print("-----------------------------------------------------------------------")
print("")
print("*Respete las mayusculas*")
print("")

contraseña = input("Cree una Contraseña: ")

print("")
print("")
print("")

verificacion = input("Verifique su contraseña: ")

print("")
print("")

if contraseña == verificacion:
    print("Se ha verificado tu contraseña")
else:
    print("La Contraseña no es la misma en la verificacion")

