"""ejercicio5 
    Escriba un programa que pruebe si la contraseña es segura 
"""
   
cadena = input("Introduzca una contraseña: ")
if len(cadena) < 8:
    print("La contraseña no es segura")
else:
    mayus = False
    minus = False
    num = False
    for i in cadena:
        if i.isupper():
            mayus = True
        elif i.islower():
            minus = True
        elif i.isnumeric():
            num = True
    if mayus and minus and num:
        print("La contraseña es segura ")  
    else:
        print("La contraseña no es segura")          
                