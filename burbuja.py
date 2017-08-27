# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:07:50 2017

@author: Luis Nerio
"""

import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo


def burbuja(arreglo):
    swap_count = 1
    while True:
        swap_count=0
        for i in range(len(arreglo)-1):
            swap_count = swap_count + swap(arreglo, i,i+1)
        if swap_count == 0 :
            break
    return arreglo
        


def swap(arreglo, l,u):
    if arreglo[l]>arreglo[u]:
        aux=arreglo[l]
        arreglo[l]=arreglo[u]
        arreglo[u]=aux
        return 1
    else:
        return 0
    
