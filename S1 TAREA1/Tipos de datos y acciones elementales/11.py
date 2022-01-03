#Dado un (1) número de cuatro (4) dígitos imprimirlo por separado
#en unidades,decenas, centenas y unidades de mil.
num = int(input("Ingresar 4 números: "))
umil= num/1000
x= num%1000

cent= x/100
y = x%100

dec= y/10

unid= num%10

print("Unidad: {}".format(int(unid)))
print("Decena: {}".format(int(dec)))
print("Centena: {}".format(int(cent)))
print("Unidad de Mil: {}".format(int(umil)))