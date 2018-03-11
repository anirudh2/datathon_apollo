# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:44:35 2018

@author: lengchun
"""

import numpy as np
from numpy import arange,array,ones,linalg
#from pylab import plot,show
import pdb
import util
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#gen_func = util.generate_A_and_b()
gen_func = util.generate_A_census_timeSer()
A, y = gen_func.generate() # Make A, b once we figure out what file we want to use for b
#pdb.set_trace()

A = np.asarray(A)
A_oneVect = np.sum(A,1)
ones_vec = np.ones((10,1))
A_mat = np.c_[A_oneVect,ones_vec]
A_mat = A_mat.T;

#A = np.asarray(A)
#ones_vec = np.ones((1,50))
#A_mat = np.r_[A,ones_vec]

y0 = [tmp[0] for tmp in y]
w= linalg.lstsq(A_mat.T,y0)[0] # Don't need to transpose A. Also, why are we taking the value at 0?

# plotting the line
line = np.matmul(A_mat.T, w) # regression line
r2_scr = r2_score(y0, line)

plt.plot(A_oneVect,line,'r-',A_oneVect,y0,'o')
plt.xlabel('Total Overdose Deaths')
plt.ylabel('Civilian labor force')
plt.show()
print(w)
print(r2_scr)

plt.plot(y0,line,'bo-', [17500, 37500],[17500, 37500],'r-')
plt.xlabel('True')
plt.ylabel('Predicted')

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
