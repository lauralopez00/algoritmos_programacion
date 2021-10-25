"""
Desarrolle un algoritmo, que dado como dato una temperatura en grados 
Fahrenheit, determine el deporte que es apropiado practicar a esa temperatura, 
teniendo en cuenta la siguiente tabla:
"""

temp = int(input("temperatura en grados farenheit: "))
depor = ""

if temp > 85:
    depor = "Natacion"
elif (temp > 70) and (temp <= 85):
    depor = "Tenis"
elif (temp > 32) and (temp <= 70):
    depor = "Golf"
elif (temp > 10) and (temp <=32):
    depor = "Esquí"
else:
    depor = "Marcha"

print(f"se puede practicar {depor}")