# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:16:47 2017

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
                                           Insertion
Función para ordenar en de manera ascendente un arrelo mediante el algoritmo de inserción, la fun-
ción toma como unico parametro un arreglo de londitud arbitraria                        
############################################################################################
******************************************************************************************"""
def insertion(arreglo):
    operaciones = 0
    for i in range(1, len(arreglo)):
        j = i
        operaciones = operaciones + 1
        while j > 0 and arreglo[j]< arreglo[j-1]:
            aux = arreglo[j]
            arreglo[j] = arreglo[j-1]
            arreglo[j-1]=aux
            j=j-1
            operaciones = operaciones + 4
    return operaciones
            
###########################################################################
#Ejemmplo
###########################################################################
p = ran_num(100)
print("Arreglo desordenado", p)
print()
num = insertion(p)

print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(num) )
