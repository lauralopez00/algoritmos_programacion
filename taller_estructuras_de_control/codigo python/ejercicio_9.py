horas = float(input("  horas trabajadas: "))
precio_hora = float(input("precio por hora trabajada: "))
sueldo_base = float(input(" valor del sueldo base: "))
pago_hora = horas * precio_hora
impuesto = 0.2
salario_neto = pago_hora + (sueldo_base * 0.8)

print(f"sueldo base de {sueldo_base}$ (al cual se le descuenta un 20% por impuestos), trabaja {horas} horas, y la hora se le paga a {precio_hora}$.")
print(f"El salario neto es de {salario_neto}$")