#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import time
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from numpy import log as ln


# ### Exemplo 1 : x² -x -1

# In[2]:


#Definindo a função
def f(x):
    return x**2-x-1


# In[7]:


start_time = time.time()
#Valores e condições iniciais de entrada
a = 1.5;   b = 1.8
eps =1.0e-6
n = 100

#Definindo o método da secante
xlista = []
contador = 2
fa=f(a)

#Testando valores iniciais com a tolerância
if abs(fa) < eps:
    print (a)
    
fb=f(b)
if abs(fb) < eps:
    print (b)
        
    
while contador <= n:
    c = (a*fb - b*fa)/(fb-fa)
    fc = f(c)
        
        
    if abs(c-b) < eps:
        break
        
    xlista.append (c)
    contador = contador + 1
    a=b
    fa=fb
    b=c
    fb=fc
           

print (f"O número de iterações realizadas foi: {contador}")
print (f"A solução é: {c}, com precisão {eps}")

#Medição de tempo de resposta
time2 = time.time() - start_time
print(f'A quantidade de tempo de resposta foi {time2} segundos')


# In[6]:


#Ordem de convergência
def order(c):
    e = [abs(xlista[i] - c) for i in range(len(xlista))]
    
    q = [np.log(e[n+1]/e[n])/np.log(e[n]/e[n-1]) for n in range(1, len(e)-1, 1)]
    return q   
solução_order= order(c)
convergência = round(solução_order [0])
print(f"A ordem de convergência dada é:{solução_order}, isto é, a ordem de convergência dada é aproximadamente {convergência}")

 

#Constante Assintótica
def const(i):
    i= i+1
    e = [abs(xlista[i] -c) for i in range(len(xlista))]
    q = [np.log(e[n+1]/e[n])/np.log(e[n]/e[n-1]) for n in range(1, len(e)-1, 1)]
    m = [e[n+1]/(e[n]**q[i]) for n in range(1,len(e)-1,1) or i in range (1, len(q)-1, 1)]
    return m
i=0
solução_const = const(i)
constante = (solução_const [1])

print(f"A constante assintótica é dada por {solução_const}, isto é, constante é dada por {round(constante, 2)}")

