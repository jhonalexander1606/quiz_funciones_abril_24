#2. Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

def determinar_4(n):
    if n % 10 == 4:
        print("su ultimo digito es 4")
    else:
        print("su ultimo digito no es 4")

n = int(input("ingrese un numero entero: "))

determinar_4(n)