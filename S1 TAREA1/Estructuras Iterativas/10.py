# Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
# la serie termina al leer un 0.

cont = 0
sum = 0
num = 1

while num != 0:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num != 0:
        sum += num
        cont += 1
if cont == 0:
    print("No ingreso ningún número.")
else:
    prom = sum / cont
    print("El promedio de los {} número es: {}".format(cont,prom))
    