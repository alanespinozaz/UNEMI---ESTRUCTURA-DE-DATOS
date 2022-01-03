#En un estacionamiento el monto a pagar se calcula multiplicando el número de
#horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
#incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
#Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada 
#y la hora de salida de un vehículo (las mismas corresponden a un mismo día) 
#calcule el monto a pagar por el dueño del vehículo.
#La entrada vendrá dada por dos enteros positivos el primero representa las horas 
#y el segundo los minutos, además por último se debe leer un carácter (A o P) que 
#indica si la hora es AM o PM.

est_inc = 4
incr_est = 2.5 

while True:
    horas = int(input("Ingrese las horas que estubo en el estacionamiento: "))
    mint = int(input("Ingrese los minutos que estubo en el estacionamiento: "))
    if mint > 0 and mint < 30:
        horas += incr_est
    pago_total = horas * incr_est
    print("Total a pagar por{} horas es ${}".format(horas, pago_total))
    x = input("¿Otro cálculo")
    if x == 'n' or x == 'N':
        break


