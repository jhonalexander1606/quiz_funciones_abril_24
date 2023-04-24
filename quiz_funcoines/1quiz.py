#1. tabla de un numero

def generar_tabla(mult,x):

    print(f"TABLA DEL {mult}")

    for i in range (x):
        print(f"{i+1} X {mult} = ",(i+1) * mult )

mult = int(input("ingrese la tabla del numero que quiere: "))

x = 10

generar_tabla(mult,x)