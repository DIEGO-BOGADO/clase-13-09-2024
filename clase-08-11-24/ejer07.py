"""Ejercicio 08
Calcular el factorial de un número dado
Ejemplo:
    5! = 1 * 2 * 3 * 4 * 5 = 120
"""
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número para calcular su factorial: "))

# Calcular el factorial
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {numero} es {factorial(numero)}")
