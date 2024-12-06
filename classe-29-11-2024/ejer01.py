"""_
Calcular el perimetro y area de un triangulo
"""
import math
# Funcion para calcular el perimetro de un triangulo 
def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

# Funcion para calcular el area de un triangulo
def area_triangulo(lado1, lado2, lado3):
    s = (lado1 + lado2 + lado3) / 2
    return math.sqrt(s + (s - lado1) + (s - lado2) +(s - lado3))

def es_triamgulo(lado1,lado2,lado3):
    return lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1
def main():
    lado1 = float(input("Lado1: "))
    lado2 = float(input("lado2: "))
    lado3 = float(input("lado3: "))
    if es_triamgulo(lado1,lado2,lado3):
      print(f"Perimetro de un triangulo es: {perimetro_triangulo(lado1,lado2,lado3):.2f}")
      print(f"Area de un triangulo es: {area_triangulo(lado1,lado2,lado3):.2f}")
    else:
        print("!!No es un triangulo!!")




if __name__=="__main__":
    main()


def calcular_area_perimetro_cuadrado(lado):
  """Calcula el área y perímetro de un cuadrado dado su lado.
  """

  area = lado * lado
  perimetro = 4 * lado
  return area, perimetro

# Solicita al usuario que ingrese la medida del lado
lado = float(input("Ingrese la medida del lado del cuadrado: "))

# Llama a la función para calcular el área y perímetro
area, perimetro = calcular_area_perimetro_cuadrado(lado)

# Imprime los resultados
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)