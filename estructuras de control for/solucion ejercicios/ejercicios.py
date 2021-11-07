archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
paises=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for q in range(b+2,len(i)):
    lista.append(i[q])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
for i in ciudad:
   if(i[0]=="U"):
    print(i)
  """
#Cuente e imprima cuantos paises que hay en el archivo
"""
n = 0
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  n += 1
  print(f"{n}. {a}")
  lista=[]
print("\nLa cantidad de paises es:",n,"\n")
"""
#Busque e imprima la ciudad de Singapur
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(c)
print(Singapur)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
paises=[]
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for q in range(b+2,len(i)):
    lista.append(i[q])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="V")and(i[1]=="e"):
    print(i)
for i in capital:
   if(i[0]=="C") and (i[1]=="a") and (i[3]=="a"):
    print(i)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[]
for i in archivo:
  a=len(i)
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
n = 0
print()
for i in paises:
  if(i[0]=="E"):
    a=i.index(":")
    n += 1
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a="".join(lista)
    print(f"{n}. {a}", end="")
  lista=[]
print("ciudades en donde su pais inicia con la letra E:",n,"\n")
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
capital=[]

for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  capital.append(a)
  lista=[]

for i in capital:
  if(i[0]=="B") and (i[1]=="o") and (i[2]=="g"):
    print(i)
  """
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
"""
with open('paises.txt') as archivo:
    lineas=archivo.readlines()
print(lineas)
for i in lineas:
    print(i.replace('rey julien','Antananarivo'))

archivo.close()
"""
#Agregue un país que no esté en la lista
"""
with open('paises.txt', 'a') as File:
    File.write('\n')
    File.write('benie:santa cruz ')
archivo.close()
"""
