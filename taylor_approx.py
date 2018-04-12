#!/usr/bin/env python3

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW07
###Exercise 2

import numpy as np
import array_calculus as ac

"""taylor_approx:
This python file contains a function that approximates f(x) using
a taylor expansion.  Additionally, this file contains the functions to
be approximated with the taylor expansion.
"""

def taylor(x,f,i,n):
    """taylor(x,f,i,n):
    This function approximates the function f over the domain x,
    using a taylor expansion centered at x[i]
    with n+1 terms (starts counting from 0).
    
    Args:
        x: The domain of the function
        f: The function that will be expanded/approximated
        i: The ith term in the domain x that the expansion is centered around
        n: The number of terms in the expansion (n+1 terms)
    Returns:
        (x,fapprox): A pair of numpy arrays where x is the original domain array and
        f approx is the approximation of f over all of the domain points x using the
        taylor expansion.
    """
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
    """tanh(x):
    This function computes tanh(x)
    Args:
        x: Domain points
    Returns:
        tanh(x): The values of tanh(x) evaluated over the domain, x.
    """
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def f(x):
    """f(x):
    This function computes (x**2/10)+sin(2x)/2
    Args:
        x: Domain points
    Returns:
        f(x): the values of the aforementioned function 
              evaluated over the domain, x.
    """
    return (x**2/10)+np.sin(2*x)/2

def inverse(x):
    """inverse(x):
    This function computes 1/x
    Args:
        x: Domain points
    Returns:
        1/x: 1/x evaluated over the domain x
    """
    if x = 0:
        f = np.nan
    else:
        f = 1/x
    return f

def ht(x):
    """ht(x)
    Evaluates the heaviside function
    Args:
        x: Domain points
    Returns:
        ht(x): Heaviside function evaluated over the domain x
    """
    if x < 0:
        f = 0
    elif x > 0:
        f = 1
    elif x == 0:
        f = .5
    return f