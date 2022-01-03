#Para un valor entero positivo que representa una cantidad en segundos, indicar
#su equivalente en minutos, horas y días.
seg = int(input("Ingrese la cantidad de segundos: "))
dias = seg //(24*60*60)
seg = seg % (24*60*60)
hor = seg //(60*60)
seg = seg % (60*60)
mint = seg // 60

print("Días: {}, Horas: {}, Minutos: {}".format(dias, hor, mint)) 