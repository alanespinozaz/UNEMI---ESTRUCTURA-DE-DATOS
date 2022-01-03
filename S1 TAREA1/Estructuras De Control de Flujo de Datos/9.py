# Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
# número.

mes = int(input("Ingrese un número entre 1 al 12: "))

if mes == 1:
    print("{}: Enero".format(mes))
elif mes == 2:
    print("{}: Febrero".format(mes))
elif mes == 3:
    print("{}: Marzo".format(mes))
elif mes == 4:
    print("{}: Abril".format(mes))
elif mes == 5:
    print("{}: Mayo".format(mes))
elif mes == 6:
    print("{}: Junio".format(mes))
elif mes == 7:
    print("{}: Julio".format(mes))
elif mes == 8:
    print("{}: Agosto".format(mes))
elif mes == 9:
    print("{}: Septiembre".format(mes))
elif mes == 10:
    print("{}: Octubre".format(mes))
elif mes == 11:
    print("{}: Noviembre".format(mes))
elif mes == 12:
    print("{}: Diciembre".format(mes))
else:
    print("Opción invalida")
