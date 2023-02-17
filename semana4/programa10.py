"""
    Programa10
    Nombre: Esquivel Cruz José David
    Fecha: 7/02/2023
    Descripcion: Programa que imprima numero mayor o none si son iguales (Ulitizacion de Unit Test)
"""

n1 = int(input("Numero 1: ")) # Peticion de un valor entero (int)
n2 = int(input("Numero 2: ")) # Peticion de un valor entero (int)

# Forma 1
if ((n1)-(n2))>0: # if con la condicio de "si la resta de n2 a n1 es mayor a cero"
	print(n1) # Accion que se realiza si la condicion de arriba se cumple
elif ((n2)-(n1))>0: # elif con la condicio de "si la resta de n1 a n2 es mayor a cero"
	print(n2) # Accion que se realiza si la condicion de arriba se cumple
else: # Si ninguna de las dos condiciones anteriores no se cumple
	print(None) # Accion que se realiza si la condicion de arriba se cumple

# Forma 2
if ((n1)-(n2))>0: # if con la condicio de "si la resta de n2 a n1 es mayor a cero"
	print(n1) # Accion que se realiza si la condicion de arriba se cumple
elif ((n2)-(n1))>0: # elif con la condicio de "si la resta de n1 a n2 es mayor a cero"
	print(n2) # Accion que se realiza si la condicion de arriba se cumple
elif n2-n1==0: #elif con la condicion de "si la resta de n1 a n2 es igual a 0"
	print(None) # Accion que se realiza si la condicion de arriba se cumple

# Forma 3
if n1<n2: # if con la condicion de "si n1 es menor a n2"
    print(n2) # Accion que se realiza si la condicion de arriba se cumple
if n2<n1: # if con la condicion de "si n2 es menor a n1"
    print(n1) # Accion que se realiza si la condicion de arriba se cumple
if n2==n1: # if con la condicion de "si n2 es igual a n1"
    print(None) # Accion que se realiza si la condicion de arriba se cumple

# Forma 4
if n1<n2: # if con la condicion de "si n1 es menor a n2"
    print(n2) # Accion que se realiza si la condicion de arriba se cumple
if n1>n2: # if con la condicion de "si n1 es mayor a n2"
    print(n1) # Accion que se realiza si la condicion de arriba se cumple
if n2==n1: # if con la condicion de "si n2 es igual a n1"
    print(None) # Accion que se realiza si la condicion de arriba se cumple

# Forma 5
if n1<=n2: # if con la condicion de "si n1 es menor o igual a n2"
    if n1==n2: # if con la condicion de "si n1 es igual a n2"
        print(None) # Accion que se realiza si la condicion de arriba se cumple
    else: # else si la condicion del if no se cumple
        print(n2) # Accion que se realiza si la condicion de arriba se cumple
else: # else si la condicion del if no se cumple
    print(n1) # Accion que se realiza si la condicion de arriba se cumple
    
# Forma 6
if n1>n2:  # if con la condicion de "si n1 es mayor a n2"
    print(n1) # Accion que se realiza si la condicion de arriba se cumple
elif n2>n1:  # elif con la condicion de "si n2 es mayor a n1"
    print(n2) # Accion que se realiza si la condicion de arriba se cumple
elif n1==n2: # elif con la condicion de "si n1 es igual a n2"
    print(None) # Accion que se realiza si la condicion de arriba se cumple

# Forma 7
if n1>=n2: # if con la condicion de "si n1 es mayor o igual a n2"
    if n1==n2: # if con la condicion de "si n1 es igual a n2"
        print(None) # Accion que se realiza si la condicion de arriba se cumple
    else: # else si la condicion del if no se cumple
        print(n1) # Accion que se realiza si la condicion de arriba se cumple
else: # else si la condicion del if no se cumple
    print(n2) # Accion que se realiza si la condicion de arriba se cumple
