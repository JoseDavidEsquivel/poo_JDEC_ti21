"""
    Programa8
    Nombre: Esquivel Cruz José David
    Fecha: 30/01/2023
    Descripcion: Utilidades del if y operadores
"""

n1= int(input("numero 1: "))
n2= int(input("numero 2: "))

""" ------------------------------
if condicion:
    codigo
----------------------------------
if condicion1:
    codigo1
else:
    codigo2
----------------------------------
Operadores Aritmeticos
+ - / * // % **
Operadores de Asignacion
=, +=, -=, /=, *=, //=, %=, **=

n=10     # (n=10)
n+=5     # (n=n+5)
n-=5     # (n=n-5)
n/=2     # (n=n/2)
n*=2     # (n=n*2)
n//3     # (n=n//3)
n%=3     # (n=n%3)
n**3     # (n=n**3)

print(n)

Operadores de comparacion
>, <, >=, <=, !=, ==

Operadores logicos
and, or, not

Operadores de Membresia (Membership)
in - not in 

5 in [0,5,14,3] -------> false
3 in [0,5,14,3] -------> true

5 not in [0,5,14,3] -------> true
3 not in [0,5,14,3] -------> false
"""

if n1>n2:  # If son una estructura de control condicional, enfrente del if se coloca la condicion
    print("hola")
else: # Si la condicion de arriba no se cumple se hace el codigo ligado al "else"
    print("adios")
