precio_lote = float(input("precio del lote de naranjas: "))
precio_docena = float(input("precio de la docena: "))
num_ventas = int(input("numero de ventas: "))
porcentaje_lote = precio_lote / precio_docena
ganancia_naranjas = porcentaje_lote + precio_lote
porcentaje_ganancias = round(num_ventas / ganancia_naranjas, 2)
print(f"el porcentaje de ganancia fue de {porcentaje_ganancias}%")
