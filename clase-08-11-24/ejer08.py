"""Ejercicio 09
Calcular el factorial de un número dado con recursividad
Ejemplo:
    5! = 1 * 2 * 3 * 4 * 5 = 120
"""
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número para calcular su factorial: "))

# Verificar que el número no sea negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    # Calcular el factorial
    print(f"El factorial de {numero} es {factorial(numero)}")
