"""ejercicio 8
escribir un programa que pida datos por teclado y de su tipo de datos  
"""

dat = input("introduce un dato: ")
print("raw", type(dat), dat)
try:
    ent = int(dat)
    print("int", type(ent), ent)
except:
    print("error! no es un dato entero")

try:
    flt = float(dat)
    print("float", type(flt), flt)
except:
    print("error! no es un dato decimal")            