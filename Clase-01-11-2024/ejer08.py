"""Ejercicio 07
Simular el telebingo y que se genere 8 numeros aleatorios de 1 al 20 y que el usuario tenga 5 numeros para acertar
y que imprima el numero de aciertos
"""
from random import randint
#numeros del bingo 
bingo = set()

while len(bingo) < 8:
    bingo.add(randint(1, 20))

usuario = set()
aciertos = 0 
while len(usuario) < 5:
    usuario.add(int(input("Introduce un numero: "))) #ingreso los numeros del usuario
print("Numeros del Bingo:")
print(bingo)
for i in bingo:
    if i in usuario:
        aciertos += 1
print(f"Tienes {aciertos} aciertos ")
if aciertos == 5:
    print("HAS GANADO")
else:
    print("Mejor suerte para la proxima")     
        