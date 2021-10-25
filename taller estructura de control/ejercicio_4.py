"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a un 
fabricante de refacciones. La empresa dependiendo del monto total de la compra, 
decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede 
de  $5.000.000  COP  la  empresa  tendrá  la  capacidad  de  invertir  de  su  propio 
dinero  un 5 5 % del monto de la compra, pedir presta al banco un 30% y el resto lo 
pagará  solicitando  un  crédito  al  fabricante.  Si  el  monto  total  de  la  compra  no 
excede  de $5.000.000 COP la empresa tendrá capacidad de invertir de su propio 
dinero  un  70%  y  el  restante  30%  lo  pagará  solicitando  crédito  al  fabricante.  El 
fabricante  cobra  por  concepto  de  intereses  un  20%  sobre  la  cantidad  que  se  le 
pague  a  crédito.      Calcule  y  muestre  la  cantidad  a  invertir  de  los  fondos  de  la 
empresa,  la  cantidad  a  pagar  a  crédito,  el  monto  a  pagar  por  intereses  y  si  es 
necesario, la cantidad prestada al banco.
"""

piezas=int(input("ingrese el numero de piezas: "))
costo_p=int(input("ingrese en costo de las piezas: "))
total=piezas*costo_p

if total>5000000:
    inversion=total*0.55
    banco=total*0.30
    credio_f=total*0.15
elif total<5000000:
    inversion=total*0.70
    credito_f=total*0.30
    banco=0

interes=credito_f*0.20

print("la inversion es de: ", inversion)
print("el prestamo del banco es de: ", banco)
print("el credito a pagar es por: ", credito_f)
print("el interes por el credito es de: ", interes)

