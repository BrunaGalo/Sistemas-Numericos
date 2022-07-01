#!/usr/bin/env python
# coding: utf-8


import numpy as np
import math


def Trapézio (n,f,a,b):
    if n == 0 :
        print ("Divisão por zero")
    elif n < 0:
        print ("Intervalo inválido")
    else:
        h = (b-a)/n
        x = a + h
        soma = 0
        for i in range (1,n):
            soma = soma + f(x)
            x = x + h
            
        R = h*(((f(a)+ f(b))/2) + soma)
        print (f"{soma}")
        print(f"{f(a)}, {f(b)}")
        print (f"O resultado da integral da função f:{R}")


#Exemplo 2
def f(x):
    return (np.e**(x))*math.sin(x)





Trapézio (4, f, 0, np.pi)





#Exemplo 3
def f(x):
    return(np.e**-(x**2))




Trapézio (256, f, 0, 1)

:




