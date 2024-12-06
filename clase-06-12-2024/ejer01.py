def es_anagrama(palabra1, palabra2):
    """

    Verifica si dos palabras son anagramas.
    :param palabra1 : primera palabra.
    :param palabra2: segunda palabra.
    :return: true si son anagramas, false en caso contrario
    """

    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")


    return sorted(palabra1) == sorted(palabra2)




    if __name__ == "main":
     palabra1 = input("Ingrese la primera palabra o frase: ")
     palabra2 = input("Ingrese la segunda palabra o frase: ")
     
     if es_anagrama(palabra1, palabra2):
         print(f"'{palabra1}' y '{palabra2}' son anagramas.")
     else:
         print(f"'{palabra1}' y '{palabra2}' no son anagramas.")
             