"""
en  una  tienda  efectúan  un  descuento  a  los  clientes  dependiendo  del  monto  de 
la compra.  El descuento se efectúa con base en el siguiente criterio
"""

compra=int(input("digite la compra: "))

if compra <50000:
    pagar=compra
elif compra <= 100000:
    pagar=compra-(compra*0.05)
elif compra <= 700000: 
    pagar=compra-(compra*0.11)
elif compra <= 1500000:
    pagar=compra-(compra*0.18)
elif compra>1500000:
    pagar=compra-(compra*0.25)

print("el total a pagar es de: ", pagar)