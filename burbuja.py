# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:07:50 2017

@author: Luis Nerio
"""

import random

"""******************************************************************************************
############################################################################################

Función para crear números aleatorios, toma como parametros n, que es la cantidad de números
que deseas y  lim_inf y lim_sup que son parametros para indicar el intervalo en el que deben
estar los números aleatorios generados
############################################################################################
******************************************************************************************"""
def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []                  
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo




"""******************************************************************************************
############################################################################################
                                        Burbuja
Función para ordenar un arreglo con algoritmo burbuja, toma como parametros un arreglo
############################################################################################
******************************************************************************************"""
def burbuja(arreglo):
    swap_count = 1                                                  ##Variable utilizada para saber cuantas veces se realiza un cambio de posición de valores
    global operaciones
    operaciones = 0 
    while True:
        swap_count=0
        for i in range(len(arreglo)-1):
            operaciones = operaciones + 1
            swap_count = swap_count + swap(arreglo, i,i+1)
        
        if swap_count == 0 :
            break
    return operaciones
        

"""******************************************************************************************
############################################################################################
                                            swap
Función que realiza un intercambio de posición de valores dentro de un arreglo, toma como parametros
el arreglo  y los indices de los valores a cambiar
############################################################################################
******************************************************************************************"""
def swap(arreglo, l,u):
    if arreglo[l]>arreglo[u]:
        global operaciones
        operaciones = operaciones + 3
        aux=arreglo[l]
        arreglo[l]=arreglo[u]
        arreglo[u]=aux
        return 1
    else:
        return 0



###########################################################################
#Ejemmplo
###########################################################################
p = ran_num(10)
print("Arreglo desordenado", p)
print()
num = burbuja(p)

print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(num) )
