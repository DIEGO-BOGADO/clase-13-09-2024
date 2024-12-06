import math
# Funcion para verificar si los lados pertenecen a un triangulo
from ejer01 import es_triamgulo
#
from ejer01 import perimetro_triangulo
#
from ejer01 import area_triangulo
#
from ejer02 import calcular_area_perimetro_cuadrado
#
from ejer03 import calcular_area_perimetro_rectangulo
#
from ejer04 import calcular_area_perimetro_circulo


def main():
    print("Calculo de perimetros y areas de poligonos")
    print("1. Triangulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Circulo")
    print("5. Salir")
  

while True:
    opcion = int(input("\nSeleccione una opcion: ")) 
    if opcion == 1:
        lado1 = float(input("Lado1: "))
        lado2 = float(input("lado2: "))
        lado3 = float(input("lado3: "))
        if es_triamgulo(lado1,lado2,lado3):
            print(f"Perimetro del triangulo:{perimetro_triangulo(lado1,lado2,lado3):.2f}")
            print(f"area del triangulo:{area_triangulo(lado1,lado2,lado3):.2f}")
        else:
            print("No es un triangulo")
    elif opcion == 2:
        lado = float(input("ingrese un el lado del cuadrado:"))
        area, perimetro = calcular_area_perimetro_cuadrado(lado)
        print("El área del cuadrado es:", area)
        print("El perímetro del cuadrado es:", perimetro)
    elif opcion == 3:
           largo = float(input("Ingrese el largo del rectángulo: "))
           ancho = float(input("Ingrese el ancho del rectángulo: "))
           print(f"El área del círculo es:, {area:.2f}")
           print(f"El perímetro del círculo es:,{perimetro:.2f}")
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area, perimetro = calcular_area_perimetro_circulo(radio)
        print(f"El área del círculo es:, {area:.2f}")
        print(f"El perímetro del círculo es:,{perimetro:.2f}")
    elif opcion == 5:
        print("Saliendo del programa...")    
       
                    
        
        



