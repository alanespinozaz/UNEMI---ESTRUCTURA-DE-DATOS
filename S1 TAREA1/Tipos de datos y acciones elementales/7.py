#Dado un número, imprimir 0 si es par y 1 si es impar.
num = int(input('Ingrese un número: '))
if num % 2 == 0:
    print("El número {} es par".format(num))
else:
    print("El número {} es impar".format(num))