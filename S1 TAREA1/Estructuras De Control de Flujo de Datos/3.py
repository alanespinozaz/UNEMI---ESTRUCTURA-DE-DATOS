#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
#resultado su equivalente en segundos.
hora = int(input("Ingrese la hora: "))
minut = int(input("Ingrese los minutos: "))
horTotal = str(hora)+":"+str(minut)
resul1 = hora* (3600//1)
resul2 = minut * (60//1)
seg = resul1 + resul2
print("Los segundos de {} son: {} segundos.".format(horTotal, seg))
