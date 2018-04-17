#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#Devon Ball
#2313078
#dball@chapman.edu
#PHYS220 Spring 2018
#CW07
###

import numpy as np
import taylor_approx as tp
import nose

def test_taylor_approx_acc():
    x = np.array([3,4,5,6,7,8])
    f = tp.tanh(x)
    trial = tp.taylor(x,f,0,100)[1] #returns 2 arrays, takes the second entry
    actual = tp.tanh(3)
    print("Trial: ", trial[0])
    print("Actual: ", actual)
    nose.tools.assert_almost_equal(actual, trial[0], 2)
    
    x = np.array([3,4,5,6,7,8])
    func = np.vectorize(tp.inverse)
    f = func(x)
    trial = tp.taylor(x,f,0,100)[1]
    actual = tp.inverse(3)
    print("Trial: ", trial[0])
    print("Actual: ", actual)
    nose.tools.assert_almost_equal(actual, trial[0], 2)
    
    x = np.array([3,4,5,6,7,8])
    func = np.vectorize(tp.f)
    f = func(x)
    trial = tp.taylor(x,f,0,100)[1]
    actual = tp.f(3)
    print("Trial: ", trial[0])
    print("Actual: ", actual)
    nose.tools.assert_almost_equal(actual, trial[0], 2)
    
def test_taylor_approx_x():
    x = np.array([3,4,5,6,7,8])
    f = tp.tanh(x)
    trial = tp.taylor(x,f,0,100)[0]
    actual = x
    print("Trial: ", trial)
    print("Actual: ", actual)
    np.testing.assert_equal(actual, trial)
    
    x = np.array([3,4,5,6,7,8])
    func = np.vectorize(tp.inverse)
    f = func(x)
    trial = tp.taylor(x,f,0,100)[0]
    actual = x
    print("Trial: ", trial)
    print("Actual: ", actual)
    np.testing.assert_equal(actual, trial)
    
    x = np.array([3,4,5,6,7,8])
    func = np.vectorize(tp.f)
    f = func(x)
    trial = tp.taylor(x,f,0,100)[0]
    actual = x
    print("Trial: ", trial)
    print("Actual: ", actual)
    np.testing.assert_equal(actual, trial)