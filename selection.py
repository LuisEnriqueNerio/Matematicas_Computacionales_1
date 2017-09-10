# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:30:22 2017

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
                                    Selection
Función para ordenar un arreglo con el algoritmo de selección, toma como parametro un 
arreglo arbitrario
############################################################################################
******************************************************************************************"""
def selection(arreglo):
    global operaciones
    operaciones = 0
    for i in range(0, len(arreglo)-1):
        operaciones = operaciones + 1
        valor_minimo = i
        for j in range(i+1, len(arreglo)):
            operaciones = operaciones + 1
            if arreglo[j]< arreglo[valor_minimo]:
                operaciones = operaciones + 1
                valor_minimo = j
        operaciones = operaciones + 1
        if valor_minimo != i:
            aux = arreglo[i]
            arreglo[i] = arreglo[valor_minimo]
            arreglo[valor_minimo] = aux
            operaciones = operaciones + 3
    return operaciones
        
###########################################################################
#Ejemmplo
###########################################################################

p = ran_num(100)
print("Arreglo desordenado", p)
print()
num = selection(p)
print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(num) )
