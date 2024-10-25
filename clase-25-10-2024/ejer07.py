"""ejercicio 3b
escriba un programa que genere 10 numeros aleatorios y devuelva el mayor y menor 
"""
from random import randint

lista = []
while len(lista) < 10:
    lista.append(randint(0, 100))
    
 """c=0
 while c<10:
   lista.append(randint(0, 100))   # genera numeros de cero a 99
   c+=1
 """
# for i in range(10):
#       lista.append(randint(50, 100))  # genera de 50 a 99 
print("lista", lista)
print("mayor:", max(lista))
print("menor", min(lista))