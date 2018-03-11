# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:44:35 2018

@author: lengchun
"""

import numpy as np
from numpy import arange,array,ones,linalg
from pylab import plot,show
import pdb
import util

#gen_func = util.generate_A_and_b()
gen_func = util.generate_A_census()
A, y = gen_func.generate() # Make A, b once we figure out what file we want to use for b
#pdb.set_trace()

A = np.asarray(A)
#A_oneP = A[0] 
#A_mat = array([A.T, ones(50)])
#y_oneP = y[0]
ones_vec = np.ones((1,51))
A_mat = np.r_[A,ones_vec]
w = linalg.lstsq(A_mat.T,y[0])[0] # Don't need to transpose A. Also, why are we taking the value at 0?

# plotting the line
line = np.matmul(A_mat.T, w) # regression line
plot(y[0],line,'o')#,A_mat.T,y[0],'o')
print(w)
show()


#xi = arange(0,9)
#C = array([ xi, ones(9)])
## linearly generated sequence
#m = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
#w = linalg.lstsq(C.T,m)[0] # obtaining the parameters
#
## plotting the line
#line = w[0]*xi+w[1] # regression line
#plot(xi,line,'r-',xi,m,'o')
#show()
