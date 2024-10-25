"""ejercicio 02
escribir un programa que pida dos numeros y me de la suma, resta, multiplicacion, division y modulo
por eleccion por teclado
"""
print("elija la operacion que desea hacer: ")
print("1 - suma, 2 - resta, 3 - multiplicacion, 4 - division, 5 - modulo")
op = int(input("opcion:"))

if op == 1:
    print(f"la suma es: {var1 + var2}")
elif op == 2:
    print(f"la resta es: {var1 - var2}")
elif op == 3:
    print(f"la multiplicacion es: {var1 * var2}")
elif op == 4:
    if var2 != 0:
        print(f"la division es: {var1 / var2}")
    else:
        print("no se puede dividir por cero...!!")
elif op == 5:
    if var2 != 0:
        print(f"el modulo es: {var1 % var2}")
    else:                            