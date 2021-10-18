mil = 1000
dos_mil = 2000
cinco_mil = 5000
diez_mil = 10000
veinte_mil = 20000
cincuenta_mil = 50000
cien_mil = 100000
cien = 100
quinientos = 500

n1 = int(input(" billetes N1 : "))
n2 = int(input(" billetes N2 : "))
n3 = int(input(" billetes N3 : "))
n4 = int(input(" billetes N4 : "))
n5 = int(input(" billetes N5 : "))
n6 = int(input(" billetes N6 : "))
n7 = int(input(" billetes N7 : "))
n8 = int(input(" billetes N8 : "))

total_dinero = (n1 * cincuenta_mil) + (n2 * veinte_mil) + (n3 * diez_mil) + (n4 * cinco_mil) + (n5 * dos_mil) + (n6 * mil) + (n7 * quinientos) + (n8 * cien)
print(f"En el banco hay un total de {total_dinero:,}$")
