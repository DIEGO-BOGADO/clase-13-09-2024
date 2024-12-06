
Frases_palindromas = [
    "A la catalama bana1 atacala",
    "A ti no, bonita"?]

def es_palindromo(cadena):
    """
    Verifica si unA CADENA es un palindromo.
    :param cadena: cadena a verificar .
    :return: True si es un palindromo, False en caso contrario. 
    """
    
    cadena_limpia = ''.join(c for c in cadena.lower() if c.isalnum())
     
    return cadena_limpia == cadena_limpia[::-1]


#Ejemplo de uso 
if  __name__ == "_main_":
    cadena = input("Ingrese una palabra o frase: ")
    
    if es_palindromo(cadena):
        print(f"'{cadena}' es un palindromo.")
    else:
         print(f"'{cadena}' no es un palindromo.")   
    