"""ejercicio 06
escriba un programa que reciba una cantidad de numeros y devuelva el mayor 
"""
def obtener_numeros():
    numeros = []
    while True:
        entrada = input("ingrese un numero (o ' q' para salir):")
        if entrada.lower() == 'q':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("por favor, ingrese un numero valido.")
    return numeros
lista = obtener_numeros()
print(lista)
print("mayor:", max(lista))
print("menor", min(lista))