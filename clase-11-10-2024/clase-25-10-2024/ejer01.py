"""ejercicio 01
escribir un programa que pida dos numeros y me de la suma, resta, multiplicacion, division y modulo
"""
var1 = float(input("Escriba un numero: "))
var2 = float(input("Escriba un numero: "))

suma = var1 + var2
print(f"la suma es: {suma}")
resta = var1 - var2
print(f"la resta es: {resta}")
multipllicacion = var1 * var2
print(f"la multiplicacion es: {multipllicacion}")
division = var1 / var2 if var2 != 0 else 0
print(f"la division es: {division:.2f}")
modulo = var1 % var2 if var2 != 0 else 0
print(f"el modulo es: {modulo}")
