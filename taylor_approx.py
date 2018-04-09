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
    dfdx = np.matmul(d,f[i])
    fapprox = f[i] + dfdx[0]*(x-a)
    return (x,fapprox)
    