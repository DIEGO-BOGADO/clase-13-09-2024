import random

# Generamos una lista aleatoria de 13 elementos entre 1 y 99
lista_original = random.sample(range(1, 100), 13)

# Creamos listas vacías para clasificar los números
lista_pares = []
lista_impares = []
lista_multiplos_3 = []

# Clasificamos los números en las listas correspondientes
for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    if numero % 3 == 0:
        lista_multiplos_3.append(numero)

# Función para calcular el promedio de una lista
def calcular_promedio(lista):
    if len(lista) == 0:
        return None
    return sum(lista) / len(lista)

# Imprimimos los resultados para cada lista
def imprimir_resultados(lista, nombre_lista):
    print(f"\n{nombre_lista}:")
    print("Tamaño:", len(lista))
    print("Contenido:", lista)
    print("Contenido ordenado:", sorted(lista))
    print("Promedio:", calcular_promedio(lista))

# Imprimimos los resultados para todas las listas
imprimir_resultados(lista_original, "Lista original")
imprimir_resultados(lista_pares, "Lista de pares")
imprimir_resultados(lista_impares, "Lista de impares")
imprimir_resultados(lista_multiplos_3, "Lista de múltiplos de 3")