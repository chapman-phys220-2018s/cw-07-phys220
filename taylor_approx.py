#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#HW06
###Exercise 1

import numpy as np
import array_calculus as ac

def taylor(x,f,i,n):
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
    return (x,fapprox)
    