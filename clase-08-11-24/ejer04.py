"""Escriba un programa que haga la tabla de multiplicar de cualquier entero numero dado por el usuario 
    la tabla debe ser del 0 al 12
"""
numero = int(input("ingrese un numero: "))

for i in range(0,13):
    print(f"{numero} * {i} = {numero * i}")