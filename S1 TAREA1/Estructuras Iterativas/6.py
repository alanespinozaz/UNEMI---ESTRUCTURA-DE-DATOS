# Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
# informe al usuario qué valor tiene el número mayor y qué valor tiene el número
# menor, sin contar el cero (0).

lista = [1,4,8,71,69,20,0]
menor = None
mayor = None
for num in lista:
    if menor == None and mayor == None:
        menor = num
        mayor = num
    else: 
        if num < menor and num > 0:
            menor = num
        if num > mayor and num > 0:
            mayor = num
print("El numero menor es: {}".format(menor))
print("El numero mayor es: {}".format(mayor))
