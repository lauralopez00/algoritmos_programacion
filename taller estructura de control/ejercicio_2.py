# Escriba  un  algoritmo,  que  dado  como  dato  el  sueldo  de  un  trabajador,  le aplique un aumento del 15% si su salario bruto es inferior a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
sueldo=float(input("ingresa el valor del sueldo: "))

if sueldo <900000:
    aumento=sueldo*0.15
elif sueldo>900000:
    aumento=sueldo*0.12

nuevo_sueldo=aumento+sueldo
print("valor del aumento: ", aumento)
print("valor de el sueldo con aumento: ",nuevo_sueldo)


