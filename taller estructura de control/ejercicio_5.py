"""
Una empresa que comercializa cosméticos tiene organizados a sus vendedores 
en tres departamentos y ha establecido un programa de incentivos para 
incrementar su productividad. El gerente, al final del mes, pide el importe global 
de las ventas de los tres departamentos y aquellos que excedan el 33% de las 
ventas totales se les paga una cantidad extra equivalente al 20% de su salario 
bruto mensual.  Si todos los vendedores ganan lo mismo, determinar cuánto 
recibirán los vendedores de los tres departamentos al finalizar el mes.
"""

sueldo=int(input("digite su sueldo: "))
ventada=int(input("digite las ventas del departamento 1: "))
ventadb=int(input("digite las ventas del departamento 2: "))
ventadc=int(input("digite las ventas del departamento 3: "))

ventastotales=ventada+ventadb+ventadc
p33=ventastotales*0.33

if ventada>p33:
    sventada=sueldo+(sueldo*0.20)
else:
    sventada=sueldo

if ventadb>p33:
    sventadb=sueldo+(sueldo*0.20)
else:
    sventadb=sueldo

if ventadc>p33:
    sventadc=sueldo+(sueldo*0.20)
else:
    sventadc=sueldo

print("los vendedores de la venta del departamento 1 recibiran un pago de: ", sventada) 
print("los vendedores de la venta del departamento 2 recibiran un pago de: ", sventadb)
print("los vendedores de la venta del departamento 3 recibiran un pago de: ", sventadc)  