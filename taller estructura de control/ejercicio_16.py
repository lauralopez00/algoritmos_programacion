"""
Confeccionar  un  algoritmo  que  permita  resolver  una  ecuación  de  segundo 
grado, de la forma: AX2+BX+C = 0, sabiendo que el discriminante (D) se calcula con 
la fórmula: D= Bˆ2­4*A*C. El valor obtenido se evalúa y se aplica la fórmula 
correspondiente, según muestra la siguiente tabla:
"""

A=int(input("ingrese el numero A: "))
B=int(input("ingrese el numero B: "))
C=int(input("ingrese el numero C: "))

D=(B**2)-4*(A*C)
print("valor de D: ", D)
if D==0:
    x1=-B/(2*A)
    print("x1=x2= ", x1)
elif D>0:
    x1=(-B+((B**2-4*A*C)/(2*A))**1/2)
    x2=(-B-((B**2-4*A*C)/(2*A))**1/2)
    print(" x1= ", x1," x2= ", x2)
elif D<0:
    print("no tiene solucion en los reales")
