#!/usr/bin/env python3

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW07
###Exercise 2

import numpy as np
import array_calculus as ac

def taylor(x,f,i,n):
    a = x[i]
    N = np.size(x)
    fa = f[i]*np.ones_like(x)
    d = ac.derivative(x[0],x[N-1],N)
    fact = 1
    fapprox = fa
    dk = np.eye(N)
    for k in range(1,n+1):
        fact = fact*(k)
        dk = np.matmul(dk,d)
        fapprox += (dk*(x-a)**k)/fact
    return (x,fapprox)

def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def f(x):
    return (x**2/10)+np.sin(2x)/2

def inverse(x):
    if x = 0:
        f = np.nan
    else:
        f = 1/x
    return f

def ht(x):
    if x < 0:
        f = 0
    elif x > 0:
        f = 1
    elif x == 0:
        f = .5
    return f