#Un hombre desea saber cuánto dinero se generará por concepto de intereses sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP y en ese caso, desea saber cuánto dinero tendrá finalmente en su cuenta.
capital=float(input("escribe la cantidad invertida en el banco: "))
tasa=float(input("escribe la tasa de interes: "))
interes=capital*tasa
print("interes = ", interes)

if interes>100000:
    print("los interes superan los $100.000")
    print("el saldo final con intereses es de: ", capital+interes)
else:
    print("los intereses no superan los 100000")


