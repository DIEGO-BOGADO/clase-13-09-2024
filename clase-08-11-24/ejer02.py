"""Ejercicio2
Escribir un programa que calcule el iva de un producto sobre el valor de la compra total, 
siendo el iva 10% 
"""
precio = float(input("Introduce el precio del producto: "))
cantidad = float(input("Introduce la cantidad de productos: "))
total = precio * cantidad
iva = total * 0.10
print(f"El total es: {total:.2f}")
print(f"El total con iva es: {iva:.2f}")