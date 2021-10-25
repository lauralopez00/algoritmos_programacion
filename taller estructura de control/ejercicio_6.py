"""
Se tienen 4 dígitos en las variables A, B, C, D que forman un entero positivo 
N. Se desea  redondear  N  a  la  centena  más  próxima  y  mostrar  el  resultado. 
Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2, entonces N 
es 2362 y el resultado redondeado es 2400. Si N es 2342, el resultado redondeado 
será 2300 y si N es 2962, el resultado redondeado será 3000.
"""

A=int(input("digite el valor A: "))
B=int(input("digite el valor B: "))
C=int(input("digite el valor C: "))
D=int(input("digite el valor D: "))

if D > 5:
    C += 1
if C > 5:
    B += 1
if B > 5:
    A += 1

A = str(A)
B = str(B)
C = str(C)
D = str(D)
num = A + B + C + D
if len(num) > 4:
    B = str(int(B) * 0)
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D

elif len(num) > 3:
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D
print(num)
