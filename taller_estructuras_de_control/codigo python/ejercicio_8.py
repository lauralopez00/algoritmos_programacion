a = float(input("digite el primer lado del triangulo: "))
b = float(input("digite el segundo lado del triangulo: "))
c = float(input("digite el tercer lado del triangulo: "))

s = (a + b + c) / 2 #Semiperimetro del triangulo
area = round((s * (s - a) * (s - b) * (s - c)) ** (1 / 2), 2) #Area del triangulo

print(f"El traignulo con lados a({a}), b({b}), y c({c}) tiene un semiperimetro de {s}, por lo que su area es de {area}")
