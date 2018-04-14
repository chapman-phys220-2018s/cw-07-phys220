#!/usr/bin/env python3

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW07
###Exercise 2

import numpy as np
import array_calculus as ac
import matplotlib.pyplot as plt

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
    D = ac.derivative(x[0],x[N-1],N)
    fact = 1
    fapprox = fa
    Dk = np.eye(N)
    for k in range(1,n+1):
        fact = fact*k
        Dk = np.matmul(Dk,D)
        fapprox += (np.matmul(np.matmul(Dk,fa),((x-a)**k)))/fact
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
    return (x**2/10)+(np.sin(2*x)/2)

def inverse(x):
    """inverse(x):
    This function computes 1/x
    Args:
        x: Domain points
    Returns:
        1/x: 1/x evaluated over the domain x
    """
    if x == 0:
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

def plots(x,f,i,title,z=2):
    """plots(x,f,i,title,z=2)
    Evaluates taylor expansion approximations and plots values for comparison
    Args:
        x (array of floats) : Domain points
        f (array of floats) : function to be evaluated and approximated
        i (int) : index of x value to be expanded around
        title (string) : Title of the graph
        z (float) : a maximum y-axis value to allow for easier graph viewing, defaults to 2
    Returns:
        None
    """
    font = {"size":18}
    plt.title(title)
    plt.xlabel("x", fontdict = font )
    plt.ylabel("Range Values", fontdict = font)
    plt.axis([-5,5,-z,z])
    plt.legend(loc = "lower right")
    g = f(x)
    x, approx0 = taylor(x,f(x),i,0)
    x, approx1 = taylor(x,f(x),i,1)
    x, approx2 = taylor(x,f(x),i,2)
    x, approx3 = taylor(x,f(x),i,3)
    x, approx4 = taylor(x,f(x),i,4)
    x, approx5 = taylor(x,f(x),i,5)
    plt.plot(x, f(x), color = "black", label="function value")
    plt.plot(x, approx0, color = "blue", label="approx., n=0")
    plt.plot(x, approx1, color = "red", label="approx.,n=1")
    plt.plot(x, approx2, color = "orange", label="approx.,n=2")
    plt.plot(x, approx3, color = "olive", label = "approx.,n=3")
    plt.plot(x, approx4, color = "purple", label = "approx.,n=4")
    plt.plot(x, approx5, color = "pink", label = "approx.,n=5")
    plt.scatter([x[i],],[g[i]], 50, color ='black')
