# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:19:32 2017

@author: Luis Nerio
"""
import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

def minimo(arr):
    m = arr[0]
    for elemento in arr :
        if elemento < m:
            m = elemento
    arr.remove(m)
    return m
 

def ordenar(arr):
    arre_2= []
    for i in range(len(arr)-1):
        arre_2.append(minimo(arr))
    arre_2.append(arr[0])
    return arre_2


p = ran_num(100)
p_2= ordenar(p)


    