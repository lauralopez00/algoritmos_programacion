Algoritmo Inicio_ejercicio_15
	escribir "digite un numero de dos cifras"
	leer numero
	numero_str<-ConvertirATexto(numero)
	inverso<-SubCadena(numero_str,1,1)+SubCadena(numero_str,0,0)
	escribir "el numero invertido es " inverso
FinAlgoritmo
