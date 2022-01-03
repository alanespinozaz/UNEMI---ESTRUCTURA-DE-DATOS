# Construya un programa que dado un valor entero N, haga el cálculo de la función
# factorial utilizando estructuras iterativas.

num = int(input("Ingrese un número entero N: "))

def faltorial(num):
    if num == 0:
        return 1
    else:
        return num * faltorial(num - 1)
print("El factorial de {}, es: {}".format(num,faltorial(num)))
