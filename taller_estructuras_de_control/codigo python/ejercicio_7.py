metros = float(input("digite la cantidad en metros:"))

metros_pulgada = round(metros * 39.27, 2)
pulgada_pie = round(metros_pulgada / 12, 2)

print(f"{metros} metros son {metros_pulgada} pulgadas y {pulgada_pie} pies")