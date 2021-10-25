"""
Una  compañía  de  alquiler  de  automóviles  sin  conductor,  desea  calcular  y 
mostrar lo que debe pagar cada cliente, de acuerdo a las siguientes condiciones
"""
kilometros= int(input("digite los kilometros: "))
monto_fijo=50000

if kilometros <= 300:
    monto_pagado=monto_fijo

elif kilometros < 1000:
    monto_pagado=monto_fijo+70000+(30000*kilometros-300)
elif kilometros>1000:
    monto_pagado=150000+(9000*kilometros-300)

print("el monto pagado al cliente sera de: ", monto_pagado)