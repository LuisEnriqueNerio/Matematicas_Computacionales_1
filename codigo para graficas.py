# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 02:12:41 2017

@author: Luis Nerio
"""

import random
import copy

"""******************************************************************************************
############################################################################################

Función para crear números aleatorios, toma como parametros n, que es la cantidad de números
que deseas y  lim_inf y lim_sup que son parametros para indicar el intervalo en el que deben
estar los números aleatorios generados
############################################################################################
******************************************************************************************"""
def ran_num(n,lim_inf=0, lim_sup=1000):
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
##Función para ordenar un arreglo con algoritmo burbuja
def burbuja(arreglo):
##Parametros
##arreglo = arreglo de longitud arbitraria
    swap_count = 1 ##Variable contadora de los cambios en arreglo
    operaciones=0 ##n\'umero de operaciones del algoritmo
    while True:
        swap_count=0
        for i in range(len(arreglo)-1):
            operaciones = operaciones + 1
            swap_count = swap_count + swap_b(arreglo, i,i+1)
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
def swap_b(arreglo, l,u):
    ##Función para cambiar de lugar dos elementos de un arreglo, 
    ##arreglo = arrelgo arbitrario,
    ##a,b= indices del arreglo a cambiar
    if arreglo[l]>arreglo[u]:
        aux=arreglo[l]
        arreglo[l]=arreglo[u]
        arreglo[u]=aux
        return 1
    else:
        return 0
    
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
        valor_minimo = i
        for j in range(i+1, len(arreglo)):
            operaciones = operaciones + 1
            if arreglo[j]< arreglo[valor_minimo]:
                valor_minimo = j
        if valor_minimo != i:
            aux = arreglo[i]
            arreglo[i] = arreglo[valor_minimo]
            arreglo[valor_minimo] = aux
            operaciones = operaciones + 3
    return operaciones    
    
"""******************************************************************************************
############################################################################################
                                           Insertion
Función para ordenar en de manera ascendente un arrelo mediante el algoritmo de inserción, la fun-
ción toma como unico parametro un arreglo de londitud arbitraria                        
############################################################################################
******************************************************************************************"""
def insertion(arreglo):
    ##arreglo = arreglo de longitud arbitraria
    operaciones = 0##variable que cuenta operaciones del algoritmo
    for i in range(1, len(arreglo)):
        j = i
        operaciones = operaciones + 1
        while j > 0 and arreglo[j]< arreglo[j-1]:
            operaciones = operaciones + 1
            aux = arreglo[j]
            arreglo[j] = arreglo[j-1]
            arreglo[j-1]=aux
            j=j-1
    return operaciones


"""******************************************************************************************
############################################################################################
                                    Quicksort
Función para ordenar un arreglo de longitud arbitraria con el algoritmo quicsort , toma como
parametro el arreglo, el indice menor y mayor del arreglo
############################################################################################
******************************************************************************************"""
def quicksort(arreglo,low,high ):
    ##Paremetros
    ##arreglo = arreglo longitud arbitraria
    ##low indice menor de arreglo 
    ##indice mayor de arreglo
    global operaciones_q
    if low < high:
        m = particion(arreglo, low, high)    
        quicksort(arreglo,low,m-1)
        quicksort(arreglo, m+1 , high)
    return operaciones_q


"""******************************************************************************************
############################################################################################
                                    Partición
Función para realizar una subrutina del algoritmo quicksort
la función regresa el indice del valor pivote en su orden respectivo en el arreglo
############################################################################################
******************************************************************************************"""
def particion(arreglo, low, high):
    ##Paremetros
    ##arreglo = arreglo longitud arbitraria
    ##low indice menor de arreglo 
    ##indice mayor de arreglo
    global operaciones_q
    pivote = arreglo[high]
    wall = low-1
    for j in range(low, high):
        operaciones_q = operaciones_q + 5
        if arreglo[j]<pivote:
            wall = wall + 1
            swap(arreglo,wall,j)
    if(arreglo[high]< arreglo[wall+1]):
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
    ##Función para cambiar de lugar dos elementos de un arreglo, arreglo = arrelgo arbitrario,
    ##a,b= indices del arreglo a cambiar
    aux = arreglo[a]
    arreglo[a]= arreglo[b]
    arreglo[b]= aux



    
    
longitud = 2
print("Longitud arreglo", "Burbuja","Seleccion","Insertion", "Quicksort")
while (longitud < 10100):
    for repeticion in range(30):
        arreglo = ran_num(longitud)
        arreglo1, arreglo2, arreglo3, arreglo4 = copy.deepcopy(arreglo), copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo)
        bubble_op = burbuja(arreglo1)
        selection_op = selection(arreglo2)
        insertion_op = insertion(arreglo3)
        operaciones_q =0
        quicksort_op = quicksort(arreglo4,0, len(arreglo4)-1)
        print(longitud,bubble_op, selection_op,insertion_op,quicksort_op)
        
    longitud += 500
    
    
directorio = ""    
    
    
