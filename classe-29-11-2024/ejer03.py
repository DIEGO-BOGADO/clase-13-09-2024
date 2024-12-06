import math

def calcular_area_perimetro_rectangulo(largo, ancho):
  """Calcula el área y perímetro de un rectángulo dados su largo y ancho.
  """

  area = largo * ancho
  perimetro = 2 * (largo + ancho)
  return area, perimetro

# Solicita al usuario que ingrese las medidas del rectángulo
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Llama a la función para calcular el área y perímetro
area, perimetro = calcular_area_perimetro_rectangulo(largo, ancho)

# Imprime los resultados
print(f"El area del rectángulo es:, {area:.2f}")
print(f"El perimetro del rectángulo es:, {perimetro:.2f}")