# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:16:47 2017

@author: Luis Nerio
"""

import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

def insertion(arreglo):
    for i in range(1, len(arreglo)):
        j = i
        while j > 0 and arreglo[j]< arreglo[j-1]:
            aux = arreglo[j]
            arreglo[j] = arreglo[j-1]
            arreglo[j-1]=aux
            j=j-1
    return arreglo
            