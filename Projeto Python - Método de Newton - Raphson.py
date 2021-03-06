#!/usr/bin/env python
# coding: utf-8

## Método de Newton-Raphson:

##Teste 1: função f(x)= x^3 - 9x + 3 com intervalo entre [0,1]
def f(x):
    return x**3-9*x+3

#Definindo primeira derivada da função
def flinha(x):
    return 3*x**2-9



# Valor inicial
x0 = 1

# Máximo número de iterações e precisão
MX = 100
EPSL = 1e-3

for k in range(MX):
    xk = x0-f(x0)/flinha(x0)
    
    if abs(xk-x0) < EPSL:
        print(f'Número de iterações = {k}')
        print(f'A raiz encontrada é {xk} (precisão de {EPSL})')
        break
        
    x0 = xk



#Teste 2: função f(x)= x^3 - x - 1, com intervalo entre [1,2] e precisão de 10^-6
def f(x):
    return x**3-1*x-1

def flinha(x):
    return 3*x**2 -1



# Valor inicial
x0 = 1

# Máximo número de iterações e precisão
MX = 100
EPSL = 1e-6

for k in range(MX):
    xk = x0-f(x0)/flinha(x0)
    
    if abs(xk-x0) < EPSL:
        print(f'Número de iterações = {k}')
        print(f'A raiz encontrada é {xk} (precisão de {EPSL})')
        break
        
    x0 = xk


