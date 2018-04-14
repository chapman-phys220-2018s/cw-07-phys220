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

def test_taylor_approx_n():
    x = np.array([3,4,5,6,7,8])
    f = tp.f(3)
    trial = tp.taylor(x,f,2,100)
    actual = 
    print("First Trial: ", trialn1)
    print("Second Trial: ", trialn2)
    np.testing.assert_not_equal(trialn1, trialn2)