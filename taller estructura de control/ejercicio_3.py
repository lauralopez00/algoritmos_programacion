#Dados los datos A, B, C y D que representan números enteros; escriba un algoritmo que calcule el resultado de las siguientes expresiones:
A=int(input("digite el numero A: "))
B=int(input("digite el numero B: "))
C=int(input("digite el numero C: "))
D=int(input("digite el numero D: "))

if D <0:
    resultado =(A-C)**2
elif D>0:
    resultado=((A-B)**3)/D
print("el resultado es de: ", resultado)