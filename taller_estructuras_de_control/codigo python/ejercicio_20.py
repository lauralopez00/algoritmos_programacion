p = float(input("valor del computador: "))
t = float(input("valor de cada cuota: "))

total_cop = t * 12
total_diferencia_p = total_cop - p
porcentaje = (total_diferencia_p*100) / p

print(f"El porcentaje de recargo es {porcentaje}%")