"""ejercicio 04
escribir un programa que pida una cadena de caracteres y imprima la longitud de la cadena 
tambien imprimir la cadena alreves 
"""
#cad es una variable de tipo string
#input es la funcion que pide una cadena
cad = input("introduce una cadena:")
#funcion len () da el tamaño de la cadena
longitud = len(cad)
print("tiene"longitud, "caracteres")
print(f"tiene {longitud} caracteres")
#imprime la cadena alreves
print(cad{::-1})
