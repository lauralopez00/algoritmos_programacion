prestamo_bolivares = float(input(" prestamo de Bolivares: "))
intereses_pagados = float(input("porcentaje de los intereses pagados: "))

tasa_interes_anual = round(((intereses_pagados * 100) / (prestamo_bolivares * 4)), 10)

print(f"El porcentaje de cobro anual por el prestamo de {prestamo_bolivares:,} Bolivares durante 4 años es de {tasa_interes_anual}%")
