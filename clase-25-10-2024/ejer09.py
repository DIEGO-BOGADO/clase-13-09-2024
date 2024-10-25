"""ejercicio 09
escriba un programa que reciba una cantidad de numeros y devuelva el mayor 
"""


def aleatorio():
    import random
    return random.randint(1, 10)
lista = [aleatorio() for i in range(10)]
print(lista)

s = set(lista)
print(s)
s.add(11)
s.add(2)
print(s)