# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:44:35 2018

@author: lengchun
"""

from numpy import arange,array,ones,linalg
from pylab import plot,show
import pdb
import util

gen_func = util.generate_A_and_b()
A = gen_func.generate() # Make A, b once we figure out what file we want to use for b
# pdb.set_trace()


# xi = arange(0,9)
# A = array([ xi, ones(9)])
# # linearly generated sequence
# y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# w = linalg.lstsq(A.T,y)[0] # obtaining the parameters
#
# # plotting the line
# line = w[0]*xi+w[1] # regression line
# plot(xi,line,'r-',xi,y,'o')
# show()
