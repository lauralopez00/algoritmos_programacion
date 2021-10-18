num_lectura = int(input("numero actual de la lectura: "))
num_lectura_pasada = int(input("numero actual de la lectura pasada: "))
costo_kilovatio = float(input("costo del kilovatio por hora: "))
total = num_lectura - num_lectura_pasada
total_pagar = total * costo_kilovatio
print(f"total a pagar de la eletricidad es de {total_pagar}$")