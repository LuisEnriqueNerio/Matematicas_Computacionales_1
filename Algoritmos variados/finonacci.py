# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:15:40 2017

@author: Luis Nerio
"""

d={0:1, 1:1 }

ope_fib = 0
ope_fib_efi=0 
ope_fib_sim=0

def fibnc(n): ## enesimo termino
    global ope_fib
    ope_fib += 1
    if n == 0  or n == 1:
        return 1
    else:
        return fibnc(n-2) + fibnc(n-1)

    
def fibnc_eficiente(n,d): ## enesimo termino
    global ope_fib_efi
    ope_fib_efi += 1
    if n in d :
        return d[n]
    else:
        ans = fibnc_eficiente(n-2,d) + fibnc_eficiente(n-1,d)
        d[n] = ans
        return ans

def fibnc_simple(n):
    global ope_fib_sim
    if n == 0 or n ==1:
        return 1
    r, r1,r2=0,1,1
    for i in range(2,n+1):
        ope_fib_sim+=1
        r = r1+r2
        r2=r1
        r1=r
    return r
    
numero = []
op_simple=[]
op_eficiente=[]
op_recursivo=[]
for i in range(0,30):
    d = dict()
    d={0:1, 1:1 }
    ope_fib = 0
    ope_fib_efi=0 
    ope_fib_sim=0
    fibnc_simple(i)
    fibnc_eficiente(i,d)
    fibnc(i)
    numero.append(i)
    op_simple.append(ope_fib_sim)
    op_eficiente.append(ope_fib_efi)
    op_recursivo.append(ope_fib)
    
        