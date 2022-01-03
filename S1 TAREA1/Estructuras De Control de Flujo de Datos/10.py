# En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario.
monto= float(input("Ingrese el monto a pagar: "))
desc = 0.20
if monto >1000:
    pag_mont= monto*desc
    print("Su monto a pagar con el descuesto es: {:.2f}".format(pag_mont))
else:
    print("Su monto a pagar es: {}, y no valida para el descuento".format(monto))