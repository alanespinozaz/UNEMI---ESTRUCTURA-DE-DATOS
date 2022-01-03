# Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
# peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
# base en dicha secuencia se desea realizar un estudio a fin de conocer:
# Edad promedio de todas las personas en la muestra.
# Peso promedio de todas las personas en la muestra.
# Estatura promedio de todas las personas en la muestra.
# Cuántas personas hay con edad entre los 18 y 25 años.
# Cuántas personas son mayores a 36 años.
# Cuál es el promedio de peso de las personas con edades entre 18 y 35
# años.

sum, sum1, sum2, sum3, sum4, sum5 = 0, 0, 0, 0, 0, 0
cont, cont1, cont2 , cont3, cont4, cont5 = 0, 0, 0, 0, 0, 0
edad = 1 
peso = 1
estt = 1

while edad != 0 and peso != 0 and estt !=0:
    edad = int(input("Ingrese la edad de la persona: "))
    peso = int(input("Ingrese el peso de la persona: "))
    estt= float(input("Ingrese la estatura de la persona: "))
    if edad != 0:
        sum += edad
        cont += 1
    if peso != 0:
        sum1 += peso
        cont1 += 1
    if estt != 0:
        sum2 += estt
        cont2 += 1
    if edad != 0:
        if 18 <= edad <= 25:
            sum3 += edad
            cont3 += 1
    if edad != 0:
        if edad >= 36:
            sum4 += edad
            cont4 += 1
    if peso != 0:
        if 18 <= edad <= 35:
            sum5 += peso
            cont5 += 1
if cont == 0 and cont1 == 0 and cont2 == 0 and cont3 == 0:
    print("...No dígito ningún número...")
else:
    prom = sum / cont
    print("El promedio de las edades de todas las personas es: {}".format(prom))
    prom1 = sum1 / cont1
    print("El promedio del peso de todas las personas es: {}".format(prom1))
    prom2 = sum2 / cont2
    print("El promedio de la estatura de todas las personas es: {}".format(prom2))
    prom3 = sum3 / cont3
    print("El promedio de la edad entre los 18 y 25 años es: {}".format(prom3))
    prom4 = sum4 / cont4
    print("El promedio de las personas mayores a 36 años: {}".format(prom4))
    prom5 = sum5 / cont5
    print("El promedio del peso de las personas con edades entre 18 y 35 años: {}".format(prom5))