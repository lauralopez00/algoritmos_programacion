nombre = input("Ingrese el nombre: ")
num_horas = float(input("Ingrese el numero de horas trabajadas: "))
pago_horas = float(input("precio por hora trabajada: "))
numero_horas_extra = float(input("Ingrese el numero de horas extra: "))
sueldo_base = float(input("Ingrese el valor del sueldo base: "))
num_hijos = int(input("Ingrese el numero de hijos: "))

pago_horas_extra = pago_horas * 1.25
pago_forzoso = sueldo_base * 0.05
politica_habitacional = round(sueldo_base * 0.02, 2)
caja_ahorro = round(sueldo_base * 0.07, 2)
acta_academica = 250000
subsidio_hijo = round(173_000 * num_hijos, 2)
prima_hogar = 180_000
sueldo_semi_neto = round((pago_horas * num_horas) + (numero_horas_extra * pago_horas_extra) + sueldo_base, 2)

asignaciones = round(acta_academica + subsidio_hijo + prima_hogar, 2)
deducciones = round(pago_forzoso + politica_habitacional + caja_ahorro ,2)
sueldo_neto = round(sueldo_semi_neto - deducciones, 2)

print(f" las asignaciones para el trabajador equivalen a un total de {asignaciones}$ ")
print(" ")
print(f" Entonces las deducciones equivalen a un total de {deducciones}$ ")
print(" ")
print(f"entonces su sueldo neto luego de las deducciones (que quivalen a ({deducciones}$)) es de {sueldo_neto}$")
