"""
Construya un programa en Python que, dados como datos la categoría y el sueldo 
bruto del trabajador, calcule el aumento correspondiente teniendo en cuenta la 
siguiente tabla:
"""
salario_bruto = int(input("digite salario: "))
categoria = int(input("digite la categoria: "))

aumento = 0
nuevo_salario = 0

if categoria == 1:
    aumento = 1.10

if categoria == 2:
    aumento = 1.15

if categoria == 3:
    aumento = 1.20

if categoria == 4:
    aumento = 1.40

if categoria == 5:
    aumento = 1.60

str_aumento = str(round(((aumento - 1.00)) * 100)) + "%"
nuevo_salario = round(salario_bruto * aumento, 3)
print(f"salario bruto es de:  {nuevo_salario:,}$")

