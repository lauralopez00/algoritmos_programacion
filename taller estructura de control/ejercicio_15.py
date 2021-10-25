"""
Tomando como base los resultados obtenidos en un laboratorio de análisis 
clínicos, un médico determina si una persona tiene anemia o no, lo cual depende 
de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de 
hemoglobina que tiene una persona es menor que el rango que le corresponde, se 
determina su resultado como positivo y en caso contrario como negativo. La 
tabla en la que el médico se basa para obtener el resultado es la siguiente:
"""
print('Ingrese: años/meses/sexo: (H-M-otro) / hemoglobina (sin unidad)')
print("EJEMPLO: 7 0 H 12")
datos = input()
lista_datos = datos.split(" ")
ano = int(lista_datos[0])
meses = int(lista_datos[1])
if (meses == 12 and ano == 0) or (meses == 0 and ano == 1):
    ano = 1
    meses = 12
sexo = lista_datos[2].capitalize()
nive_hemoglobina = float(lista_datos[3])

if ((meses >= 0) and (meses <=1)):
    if ((nive_hemoglobina >= 13) and (nive_hemoglobina <= 26)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif ((meses > 1) and (meses <= 6)):
    if ((nive_hemoglobina >= 10) and (nive_hemoglobina <= 18)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif ((meses > 6) and (meses <= 12)):
    if ((nive_hemoglobina >= 11) and (nive_hemoglobina <= 15)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif ((ano > 1) and (ano <= 5)):
    if ((nive_hemoglobina >= 11.5) and (nive_hemoglobina <= 15)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif ((ano > 5) and (ano <= 10)):
    if ((nive_hemoglobina >= 12.6) and (nive_hemoglobina <= 15.5)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif ((ano > 10) and (ano <= 15)):
    if ((nive_hemoglobina >= 13) and (nive_hemoglobina <= 15.5)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif (ano > 15) and (sexo == "M"):
    if ((nive_hemoglobina >= 12 and (nive_hemoglobina <= 16))):
        print("Resultado (-)")
    else:
        print("Restultado (+)")
elif (ano > 15) and (sexo == "H"):
    if ((nive_hemoglobina >= 13) and (nive_hemoglobina <= 26)):
        print("Resultado (-)")
    else:
        print("Restultado (+)")