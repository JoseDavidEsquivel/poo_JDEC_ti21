"""
    Programa10
    Nombre: Esquivel Cruz José David
    Fecha: 30/01/2023
    Descripcion: Programa que imprima numero mayor o none si son iguales (Ulitizacion de Unit Test)
"""

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

# Forma 1
if ((n1)-(n2))>0:
	print(n1)
elif ((n2)-(n1))>0:
	print(n2)
else:
	print(None)

# Forma 2
if ((n1)-(n2))>0:
	print(n1)
elif ((n2)-(n1))>0:
	print(n2)
else:
	print(None)

# Forma 3
if n1<n2:
    print(n2)
if n2<n1:
    print(n1)
if n2==n1:
    print(None)

# Forma 4
if n1<n2:
    print(n2)
if n1>n2:
    print(n1)
if n2==n1:
    print(None)

# Forma 5
if n1<=n2:
    if n1==n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)

    
