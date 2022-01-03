# Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
# 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
# Enero de 2014 hasta la fecha dada.

from datetime import date

fecha = date(2013,5,28)
fecha1 = date(2013,1,1)

delta =  fecha-fecha1
print("El número de días es: ", delta.days)
print(type(fecha1))