num_estudiantes = int(input("digite el numero de estudiantes: "))
num_hombres = int(input("digite el numero de hombres:  "))
num_mujeres = int(input("digite el numero de mujeres: "))
porcentaje_hombres = round(((num_hombres * 100) / num_estudiantes), 2)
porcentaje_mujeres = round(((num_mujeres * 100) / num_estudiantes), 2)

print(f"En un salon de {num_estudiantes} estudiantes, donde hay {num_hombres} hombres y {num_mujeres} mujeres, se puede determinar que:")
print(f"El {porcentaje_hombres}% de los estudiantes de la clase son hombres, y {porcentaje_mujeres}% de los estudiantes de la clase son mujeres.")
