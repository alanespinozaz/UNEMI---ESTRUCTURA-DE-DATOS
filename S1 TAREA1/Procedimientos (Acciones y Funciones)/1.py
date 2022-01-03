# Construya una función que solicite edades al usuario y determine el promedio de
# las edades mayores a 18 años. El usuario indicará cuando desea dejar de
# suministrar datos de entrada. En la Acción Principal se informará el promedio
# calculado.

def edades():
    sum = 0
    cont = 0
    edad = 1
    while edad != 0:
        edad = int(input("Ingrese un número entero (0 para terminar): "))
        if edad != 0:
            if edad > 18:
                sum += edad
                cont += 1
    if cont == 0:
        print("No ingreso ningún número.")
    else:
        prom = sum / cont
        print("El promedio de edades mayores a 18 años es: {}".format(prom))
edades()