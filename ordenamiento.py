# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:19:32 2017

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
                                        Minimo
Función para encontrar el minimo valor de un arreglo abtrario
Toma como parametro un arreglo
############################################################################################
******************************************************************************************"""
def minimo(arr):
    global operaciones
    m = arr[0]
    operaciones = operaciones +1
    for elemento in arr :
        operaciones = operaciones + 1
        if elemento < m:
            m = elemento
            operaciones = operaciones + 1
    operaciones = operaciones + 1
    arr.remove(m)
    operaciones = operaciones + len(arr)
    return m
 
"""******************************************************************************************
############################################################################################
                                        Ordenar
Función que ordena un arreglo, toma como parametro un arreglo arbitrario
############################################################################################
******************************************************************************************"""
def ordenar(arr):
    global operaciones
    operaciones = 0
    operaciones = operaciones + 1
    arre_2= []
    for i in range(len(arr)-1):
        operaciones = operaciones + 1
        arre_2.append(minimo(arr))
    arre_2.append(arr[0])
    return arre_2


    
###########################################################################
#Ejemmplo
###########################################################################
p = ran_num(100)
print("Arreglo desordenado", p)
print()
p=ordenar(p)
print("Arreglo ordenado" ,p)
print("Número de operaciones : " + str(operaciones)) 
