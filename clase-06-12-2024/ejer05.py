"""
Crea un programa que implemente un cifrado Cesar.
Este metodo consiste en desplazar cada letra de un texto un numero fijo de posiciones en el alfabeto.
Por ejemplo, con un desplazamiento de 3, la letra 'a' se convierte en 'd', 'b' en 'e', y asi sucesivamente
Las letras deben permanecer en su caso en (mayusculas/minusculas) y los caracteres que no sean letras deben permanecer igual.
"""

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado


#Solicitar al usuario una frase y el desplazamiento
texto  = input("Introduce un texto para cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento (numero entero): "))


#Aplicar el cifrado Cesar
texto_cifrado = cifrado_cesar(texto, desplazamiento)

#Mostrar el resultado 
print(f"\nTexto cifrado: {texto_cifrado}")            
            