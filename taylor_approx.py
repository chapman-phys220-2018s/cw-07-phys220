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
    def f(x,f,i,n):
        a = x[i]
        d = ac.derivative(x[i],x[i]+100,101)
        d2 = ac.second_derivative(x[i],x[i]+100,101)
        dfdx = np.matmul(d,f[i])
        d2fdx2 = np.matmul(d2,f[i])
        if n == 0:
            fapprox = f[i]
        elif n == 1:
            fapprox = f[i] + dfdx[0]*(x-a)
        elif n == 2:
            fapprox = f[i] + dfdx[0]*(x-a) + d2fdx2[0]*((x-a)**2)/2
        else:
            return print("Invalid n, please choose a new n")
        f = np.vectorize(f)
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