frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
for i in frutas:
  lista_frutas.append(i)
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in numeros:
  lista_numeros.append(i)


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
Salidas
"""
def eliminar(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
Salidas
"""
def lista_c(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
Salidas
"""  
def enteros(lista:list):
  auxiliar=[]
  auxiliar2=[]
  for i in lista:
    auxiliar.apepend(float(i))
  for i in auxiliar:
    auxiliar2.append(int(i))
  return auxiliar2

def pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas: list: lista a modificar, str: elemento a eliminar 
Salidas: Lista original sin el elemento_elimin
"""  
def elimina_elemento_lista(lista, elemento_elimin):
  lista_sin_elemento = []
  for elemento in lista:
    if elemento == elemento_elimin:
          pass
    else: 
      lista_sin_elemento.append(elemento)
  return lista_sin_elemento

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista(str)-->list-->lista
elem-->str-->elem
Salidas:
lista letra-->list-->lista(str)
"""  
def letra(lista:list,elem:str)->list:
  aux=[]
  for i in lista:
    if(i[0]==elem):
      aux.append(i)
  return aux

#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas: list: Lista que va a ser contada
Salidas: Numero de elementos contados en la lista (tama単o de la lista)
"""   
def tamano_lista(lista):
  return len(lista)
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas: list: Lista que va a ser evaluada
Salidas: Numero de elementos contados en la lista (tama単o de la lista) inspeccionada, y el tipo de
         datos contenidos en la lista
"""  
def informacion_lista(lista):
    tamano = len(lista)
    tipo = type(lista[-1])
    return tamano, tipo

#Retornar una lista con los numero negativos  
"""
Entradas: list: lista con numero reales como elementos
Salidas: La lista ingresada pero sin los elementos POSITIVOS
"""  
def numeros_negativos(lista):
  lista_todos = []
  for numero in lista: 
    lista_todos.append(int(float(numero)))
  lista_sin_positivos = lista_todos.copy()
  for numero in lista_todos: 
    if numero < 0:
        lista_todos = lista_todos
    elif numero >= 0: 
      lista_sin_positivos.remove(numero)
    else: 
      lista_original = lista_original
  return lista_sin_positivos

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion(lista:list,elemento:str):
  for i in lista:
    if(i==elemento):
     p=lista.index(i)
     print (p)
#realizar una funcion que agregue al final de archivo frutas una fruta

Entradas:
lista(str)-->list-->frutas
elemento-->str-->elem
Salidas:
lista(str)-->list-->frutas
"""
def frutas(elem:str)->list:
  aux=open("frutas.txt","a")
  aux.write(elem)
  aux.close()
  """
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
Entradas: str: Elemento que se va a contar en la lista
Salidas: Numero de veces que aparece el elemento en la lista
"""  
def repetir(elemento):
  vLista = 0
  for i in lista_numeros:
    if i == elemento:
      vLista += 1
  return vLista

  
if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)