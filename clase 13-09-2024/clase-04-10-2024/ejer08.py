"""_sumary_
Operaciones con cadenas
Introduzca una cadena y muestre en minusculas y  mayusculas 
"""

cadena = input("cadena: ") # ingresar cadena

mayus = cadena.upper() # poner en mayuscula
minus = cadena.lower() # poner en minuscula
cap = cadena.cap() # capitalizar

print(mayus) # imprimir
print(minus) # imprimir
print(cap) # imprimir

lista = cadena.split("o") # dividir la cadena en una lista dividida por "o"

print(lista) # imprimir lista