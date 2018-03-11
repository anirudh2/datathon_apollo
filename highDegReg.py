# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:24:02 2018

@author: lengchun
"""

from numpy import *
import pylab
import pdb
import util


# data to fit
gen_func = util.generate_A_and_b()
A, y = gen_func.generate() # Make A, b once we figure out what file we want to use for b

A = asarray(A)
x = A
#pdb.set_trace()

# fit the data with a 4th degree polynomial
z4 = polyfit(x, y, 4)
p4 = poly1d(z4) # construct the polynomial

z5 = polyfit(x, y, 5)
p5 = poly1d(z5)

xx = linspace(0, 1, 100)
pylab.plot(x, y, 'o', xx, p4(xx),'-g', xx, p5(xx),'-b')
pylab.legend(['data to fit', '4th degree poly', '5th degree poly'])
pylab.axis([0,1,0,1])
pylab.show()
