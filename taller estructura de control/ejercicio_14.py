"""
Desarrolle  un  programa  en  Python  que  calcule  y  muestre  el  monto  que  debe 
pagar ar suscriptor por concepto de consumo de luz eléctrica y servicio de aseo 
urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior 
y la lectura actual por el costo de cada Kilovatio hora, según la siguiente escala:
"""

lectura_actual = int(input("lectura actual: "))
lectura_anterior = int(input("lectura anterior: "))
diferencia = abs(lectura_anterior - lectura_actual)
costo = 0

if diferencia >= 0 and diferencia <= 100:
    costo = 4_600

elif diferencia >= 101 and diferencia <= 300:
    costo = 80_000

elif diferencia >= 310 and diferencia <= 500:
    costo = 100_000

elif diferencia >= 501:
    costo = 120_000

costo_final = diferencia * costo
print(costo)
print(f"pagar {costo_final:,}")