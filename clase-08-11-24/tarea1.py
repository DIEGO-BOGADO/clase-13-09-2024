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

productos = {
    1:{"precio": 50, "iva": 10, "nombre": "teclado"},
    2:{"precio": 20, "iva": 5, "nombre": "raton"},
    3:{"precio": 80, "iva": 10, "nombre": "monitor 15"},
    4:{"precio": 110, "iva": 10, "nombre": "monitor 17"},
    5:{"precio": 135, "iva": 10, "nombre": "monitor 19"},
    6:{"precio": 40, "iva": 5, "nombre": "raton rgb"},
    7:{"precio": 70, "iva": 10, "nombre": "teclado rgb"},
    8:{"precio": 160, "iva": 10, "nombre": "monitor 21"},
    9:{"precio": 200, "iva": 10, "nombre": "monitor 27"},
}

print(productos.get(1).get("nombre"))