# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:13:14 2017

@author: Luis Nerio
"""

import random

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo

def merge(arreglo,inicio,fin):
    arreglo2= arreglo[:] ##copia del arreglo original
    merge_1(arreglo, arreglo2, inicio, fin)
    return 0
    
def merge_1(arreglo, arreglo2, inicio, fin):
    if (fin - inicio) < 1:
        return 
    
    mitad = (inicio + fin)//2
    merge_1(arreglo2,arreglo,inicio, mitad)
    merge_1(arreglo2,arreglo,mitad+1,fin)
    merge_2(arreglo, arreglo2, inicio, mitad+1, fin)
    
def merge_2(arreglo, arreglo2, inicio, mitad, fin):
  i = inicio
  j= mitad
  for k in range(inicio, fin+1):
      if i < mitad and (j>= fin+1 or arreglo2[i]  < arreglo2[j]):
          arreglo[k] = arreglo2[i]
          i = i + 1
      else:
          arreglo[k] = arreglo2[j]
          j = j + 1
