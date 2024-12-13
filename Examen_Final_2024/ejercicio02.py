def analizar_cadena(cadena):
    vocales = "aeiou"
    consonantes = "bcdfghjklmnñpqrstvwxyz"

    cantidad_vocales = 0
    cantidad_consonantes = 0
    cantidad_otros = 0
    cantidad_palabras = 1  # Iniciamos en 1 por el primer espacio
    tiene_que = False
    cantidad_mayusculas = 0
    cantidad_minusculas = 0
    cantidad_a = 0
    cantidad_f = 0

    for caracter in cadena:
        if caracter.lower() in vocales:
            cantidad_vocales += 1
        elif caracter.lower() in consonantes:
            cantidad_consonantes += 1
        else:
            cantidad_otros += 1
            if caracter.isspace():
                cantidad_palabras += 1
        if caracter == "que" or caracter == "QUE":
            tiene_que = True
        if caracter.isupper():
            cantidad_mayusculas += 1
        elif caracter.islower():
            cantidad_minusculas += 1
        if caracter.lower() == "a":
            cantidad_a += 1
        if caracter.lower() == "f":
            cantidad_f += 1

    print("Cantidad de vocales:", cantidad_vocales)
    print("Cantidad de consonantes:", cantidad_consonantes)
    print("Cantidad de otros caracteres:", cantidad_otros)
    print("Cantidad de palabras:", cantidad_palabras)
    print("Contiene la palabra 'que':", tiene_que)
    print("Cantidad de mayúsculas:", cantidad_mayusculas)
    print("Cantidad de minúsculas:", cantidad_minusculas)
    print("Cantidad de letras 'a':", cantidad_a)
    print("Cantidad de letras 'f':", cantidad_f)

# Solicitar la cadena al usuario
cadena = input("Ingrese una cadena: ")

# Analizar la cadena
analizar_cadena(cadena)