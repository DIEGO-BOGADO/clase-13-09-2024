"""Ejercicio1 
Escribir un programa que tome tres notas de un alumno y de la nota final y su calificacion.
Tenga en cuenta que la primera y segunda nota tienen peso de 30% y la tercera de 40%
"""
nota1 = int(input("ingrese la primera nota: "))
nota2 = int(input("ingrese la segunda nota: "))
nota3 = int(input("ingrese la tercera nota: "))

notafinal = (nota1 * 0.3 ) + (nota2 * 0.3 ) + (nota3 * 0.4 )

print(f"La nota final es: ",{notafinal})

if notafinal >= 6:
    print("Aprobado")
else:
    print("Reprobado")    