# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:30:22 2017

@author: Luis Nerio
"""

import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

def selection(arreglo):
    for i in range(0, len(arreglo)-1):
        valor_minimo = i
        for j in range(i+1, len(arreglo)):
            if arreglo[j]< arreglo[valor_minimo]:
                valor_minimo = j
        if valor_minimo != i:
            aux = arreglo[i]
            arreglo[i] = arreglo[valor_minimo]
            arreglo[valor_minimo] = aux
    return p
        
        