# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:13:14 2017

@author: Luis Nerio
"""

import random

"""******************************************************************************************
############################################################################################
                                            swap
Función que realiza un intercambio de posición de valores dentro de un arreglo, toma como parametros
el arreglo  y los indices de los valores a cambiar
############################################################################################
******************************************************************************************"""
def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

"""******************************************************************************************
############################################################################################
                                            Merge
Función que ordena un arreglo mediante el algoritmo merge, toma como parametros el arreglo
inicio del indice del arreglo y indice final del arreglo, regresa la longitud del arreglo ordenado y 
el número de operaciones que se  utilizo para ordenar.
############################################################################################
******************************************************************************************"""
def merge(arreglo,inicio,fin):
    global operaciones
    arreglo2= arreglo[:] ##copia del arreglo original
    operaciones = operaciones +1
    merge_1(arreglo, arreglo2, inicio, fin)
    return (len(arreglo), operaciones)
    
def merge_1(arreglo, arreglo2, inicio, fin):
    global operaciones
    operaciones = operaciones +1
    if (fin - inicio) < 1:
        return 
    mitad = (inicio + fin)//2
    merge_1(arreglo2,arreglo,inicio, mitad)
    merge_1(arreglo2,arreglo,mitad+1,fin)
    merge_2(arreglo, arreglo2, inicio, mitad+1, fin)
    operaciones = operaciones +4
    
def merge_2(arreglo, arreglo2, inicio, mitad, fin):
  global operaciones
  i = inicio
  j= mitad
  operaciones = operaciones +2
  for k in range(inicio, fin+1):
      operaciones = operaciones +1
      if i < mitad and (j>= fin+1 or arreglo2[i]  < arreglo2[j]):
          arreglo[k] = arreglo2[i]
          i = i + 1
          operaciones = operaciones +2
      else:
          arreglo[k] = arreglo2[j]
          j = j + 1
          operaciones = operaciones +2
          
          
###########################################################################
#Ejemmplo
###########################################################################
p = ran_num(100)
print("Arreglo desordenado", p)
print()
num = merge(p, 0, len(p)-1)

print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(num[1] )) 
