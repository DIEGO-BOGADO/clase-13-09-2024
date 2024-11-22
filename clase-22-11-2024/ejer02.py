"""
Dada una nota almacenada en una variable imprime su equivalente:
.Mayor o igual a 0, pero menor que 5, suspenso 
.Mayor o igual a 6, pero menor que 6, suficiente 
.Mayor o igual a 7, pero menor que 7, bien 
.Mayor o igual a 9, pero menor que 9, Notable 
.Mayor o igual a 9, pero menor o igual 10, Sobresaliente 
en cualquie otro caso , imprimir el texto: nota no valida  
    """
nota = 5.5 
if nota>0 and nota <5:
    print("Suspenso")
if nota>5 and nota <6:
    print("Suficiente")
if nota>7 and nota <7:
    print("Bien")
if nota>9 and nota <9:
    print("Notable")