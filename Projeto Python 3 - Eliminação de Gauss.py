import numpy as np
import sys

def gauss(A,n,b):
    x = np.zeros(n)
    a = np.hstack([A,b.reshape(n,1)])
    for i in range(n):
        if a[i,i] == 0.0:
            sys.exit("Não é possível realizar eliminação de Gauss sem permutaçao de linhas.")       
        for j in range(i+1, n):        
            a[j,:] = a[j,:] - a[j,i]/a[i,i] * a[i,:]
    # Retrosubsittuição
    x[n-1] = a[n-1,n]/a[n-1,n-1]

    for i in range(n-2,-1,-1):
    
        x[i] = (a[i,n] - np.dot(a[i,i+1:n], x[i+1:n]))/a[i,i]
    return A,x
