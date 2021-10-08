Algoritmo Inicio_ejercicio_18
	escribir "por favor digita tu primer nombre"
	leer nombre
	escribir "por favor digita tu segundo nombre"
	leer nombre2
	escribir "por favor digita tu primer apellido"
	leer apellido1
	escribir "por favor digita tu segundo apellido"
	leer apellido2
	nombre<-SubCadena(nombre,0,0)+SubCadena(nombre2,0,0)
	apellido<-SubCadena(apellido1,0,0)+SubCadena(apellido2,0,0)
	escribir " las iniciales de su nombre son " nombre+apellido
FinAlgoritmo
