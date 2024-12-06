
import math

def calcular_area_perimetro_circulo(radio):
  """Calcula el área y perímetro de un círculo dado su radio.
  """

  area = math.pi * radio**2
  perimetro = 2 * math.pi * radio
  return area, perimetro

# Solicita al usuario que ingrese el radio
radio = float(input("Ingrese el radio del círculo: "))

# Llama a la función para calcular el área y perímetro
area, perimetro = calcular_area_perimetro_circulo(radio)

# Imprime los resultados
print(f"El área del círculo es:, {area:.2f}")
print(f"El perímetro del círculo es:,{perimetro:.2f}")