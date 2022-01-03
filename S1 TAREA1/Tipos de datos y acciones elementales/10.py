#Dado un número binario de cuatro (4) dígitos imprimir su valor
def validar(ingreso):
    aux=True
    for r in ingreso:
        if r != '1' and r != '0':
            aux=False
            break
    return aux
ent = input("Ingrese un binario de 4 dígitos: ")
while validar(ent) == False: 
    entrada = input("Ingrese un binario de 4 digítos: ")
cad = ent[::-1]
sal = 0; expon =0;
while expon < len(cad):
    if int(cad[expon])==1:
        sal += int(cad[expon])*2**expon
    expon += 1
print("El valor del bianrio es: ", sal)
