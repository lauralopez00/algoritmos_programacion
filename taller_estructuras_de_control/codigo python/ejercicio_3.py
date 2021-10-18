#dinero que se obtendra por comisiones
print("digite el sueldo base")
sueldo_base = float(input())
venta1 = int(input("digite la primera venta"))
venta2 = int(input("digite la segunda venta"))
venta3 = int(input("digite la tercera venta"))
comision = (venta1+venta2+venta3)*0.10
dinero_total = comision+sueldo_base
print("el dinero total segun las tres ventas sera de ",dinero_total)
