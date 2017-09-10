# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:57:05 2017

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
                                    Quicksort
Función para ordenar un arreglo de longitud arbitraria con el algoritmo quicsort , toma como
parametro el arreglo, el indice menor y mayor del arreglo
############################################################################################
******************************************************************************************"""
def quicksort(arreglo,low,high ):
    global operaciones
    if low < high:
        operaciones = operaciones + 3
        m = particion(arreglo, low, high)    
        quicksort(arreglo,low,m-1)
        quicksort(arreglo, m+1 , high)
    return operaciones


"""******************************************************************************************
############################################################################################
                                    Partición
Función para realizar una subrutina del algoritmo quicksort
la función regresa el indice del valor pivote en su orden respectivo en el arreglo
############################################################################################
******************************************************************************************"""
def particion(arreglo, low, high):
    global operaciones
    operaciones = operaciones + 1
    pivote = arreglo[high]
    wall = low-1
    operaciones = operaciones + 1
    for j in range(low, high):
        operaciones = operaciones + 1
        if arreglo[j]<pivote:
            wall = wall + 1
            swap(arreglo,wall,j)
            operaciones = operaciones + 5
    operaciones = operaciones + 1
    if(arreglo[high]< arreglo[wall+1]):
        operaciones = operaciones + 3
        swap(arreglo,wall+1,high)
    return wall+1


"""******************************************************************************************
############################################################################################
                                            swap
Función que realiza un intercambio de posición de valores dentro de un arreglo, toma como parametros
el arreglo  y los indices de los valores a cambiar
############################################################################################
******************************************************************************************"""
def swap(arreglo, a, b):
    aux = arreglo[a]
    arreglo[a]= arreglo[b]
    arreglo[b]= aux


###########################################################################
#Ejemmplo
###########################################################################
global operaciones 
operaciones = 0
p = ran_num(100)
print("Arreglo desordenado", p)
print()
num = quicksort(p, 0, len(p)-1)
print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(num) )
            
