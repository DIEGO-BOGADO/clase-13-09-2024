import math

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
 
 
 
 
 