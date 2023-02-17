"""
    Programa6
    Nombre: Esquivel Cruz José David
    Fecha: 30/01/2023
    Descripcion: Area y perimetro de un triangulo dado sus 3 lados
"""

print("Introduzca las medidas de los lados de su triangulo")

lado1= int(input("Lado 1 = ")) # peticion del lado 1
lado2= int(input("Lado 2 = ")) # peticion del lado 2
lado3= int(input("Lado 3 = ")) # peticion del lado 3

perimetro = lado1 + lado2 + lado3 # operaciones de el perimetro
sp = perimetro/2 # operaciones de semiperimetro
area = sp*(sp-lado1)*(sp-lado2)*(sp-lado3) # operaciones de el area
area = area**0.5 # operaciones de el area


print(perimetro) # Impresion del Perimetro
print(area) # Impresion del Area
