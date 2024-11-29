"""Tarea 01
Escribir un programa que haga una factura de venta varios productos, calcule los ivas de 5% y 10% dependiendo del producto.
Debe dar cuanto va a pagar el cliente y el iva total de la compra
Los productos son:
nro producto    precio  iva
1   teclado      50$     10%
2   raton        20$     5%
3   monitor 15"  80$     10% 
4   monitor 17" 110$     10%
5   monitor 19" 135$     10%
6   raton rgb    40$     5%
7   teclado rgb  70$     10%
8   monitor 21" 160$     10%
9   monitor 27" 200$     10%
"""

def generar_factura():
    """Genera una factura de venta para los productos especificados."""

    # Productos y sus características
    productos = {
        1: {"nombre": "teclado", "precio": 50, "iva": 10},
        2: {"nombre": "ratón", "precio": 20, "iva": 5},
        3: {"nombre": "monitor 15\"", "precio": 80, "iva": 10},
        4: {"nombre": "monitor 17\"", "precio": 110, "iva": 10},
        5: {"nombre": "monitor 19\"", "precio": 135, "iva": 10},
        6: {"nombre": "ratón RGB", "precio": 40, "iva": 5},
        7: {"nombre": "teclado RGB", "precio": 70, "iva": 10},
        8: {"nombre": "monitor 21\"", "precio": 160, "iva": 10},
        9: {"nombre": "monitor 27\"", "precio": 200, "iva": 10}
    }

    # Inicializar variables
    total_compra = 0
    iva_total = 0

    # Solicitar al usuario la cantidad de cada producto
    while True:
        try:
            numero_producto = int(input("Ingrese el número de producto (0 para finalizar): "))
            if numero_producto == 0:
                break
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue

            # Calcular el subtotal, el IVA del producto y sumarlo al total
            producto = productos[numero_producto]
            subtotal = producto["precio"] * cantidad
            iva_producto = (subtotal * producto["iva"]) / 100
            total_compra += subtotal + iva_producto
            iva_total += iva_producto

        except KeyError:
            print("Número de producto inválido.")
        except ValueError:
            print("Ingrese un valor numérico válido.")

    # Imprimir la factura
    print("\n--- Factura de Venta ---")
    print("------------------------")
    # Aquí puedes personalizar la impresión de la factura según tus necesidades
    print(f"Total a pagar: ${total_compra:.2f}")
    print(f"IVA total: ${iva_total:.2f}")
    print("------------------------")
if __name__ == "__main__":
    generar_factura()
    