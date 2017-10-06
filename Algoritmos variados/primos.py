# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:30:43 2017

@author: Luis Nerio
"""
import math
import matplotlib.pyplot as plt


def primo (num):
    contador = 0
    test = "Primo"
    for i in range(2, math.ceil( math.sqrt(num) ) +1):
        contador += 1 
        if (num % i) == 0:
            test = "No primo"
            break
    return (contador,test)

numero_operaciones=[]
numero_checado=[]
numero_test=[]
for numero in range(1,10001,100):
    t = primo(numero)
    numero_checado.append(numero)
    numero_operaciones.append(t[0])
    numero_test.append(t[1])
for i in range(0, len(numero_checado)):
    print(numero_checado[i],numero_operaciones[i], numero_test[i])

plt.plot(numero_checado,numero_operaciones)
    
    