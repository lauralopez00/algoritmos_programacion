Algoritmo Inicio_ejercicio_8
	escribir "por favor digite la cantidad de minutos"
	leer minutos1
	horas<-trunc(minutos1/60)
	Si minutos1>60 Entonces
		minutos<-minutos1-(horas*60)
	SiNo
		minutos<-minutos
	Fin Si
	escribir minutos1 " los minutos son " horas " horas y " minutos " minutos "
	
	
FinAlgoritmo
