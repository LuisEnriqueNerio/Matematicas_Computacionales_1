# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:57:05 2017

@author: Luis Nerio
"""

import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

def quicksort(arreglo,low,high ):
    if low < high:
        m = particion(arreglo, low, high)    
        quicksort(arreglo,low,m-1)
        quicksort(arreglo, m+1 , high)

def particion(arreglo, low, high):
    pivote = arreglo[high]
    wall = low-1
    for j in range(low, high):
        if arreglo[j]<pivote:
            wall = wall + 1
            swap(arreglo,wall,j)
    if(arreglo[high]< arreglo[wall+1]):
        swap(arreglo,wall+1,high)
    return wall+1

def swap(arreglo, a, b):
    aux = arreglo[a]
    arreglo[a]= arreglo[b]
    arreglo[b]= aux
            