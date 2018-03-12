# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:44:35 2018

@author: lengchun
"""

import numpy as np
from numpy import arange,array,ones,linalg
from scipy import stats
#from pylab import plot,show
import pdb
import util
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def nan_helper(y):
    return np.isnan(y), lambda z: z.nonzero()[0]

gen_func = util.generate_A_and_b()
#gen_func = util.generate_A_census_timeSer()
A, y = gen_func.generate() # Make A, b once we figure out what file we want to use for b
#pdb.set_trace()

#A = np.asarray(A)
#A_oneVect = np.sum(A,1)
#ones_vec = np.ones((10,1))
#A_mat = np.c_[A_oneVect,ones_vec]
#A_mat = A_mat.T;

A = np.asarray(A)
ones_vec = np.ones((1,3186))
A_mat = np.r_[A,ones_vec]
y0 = np.asarray(y[0])
A_T = A_mat.T
nans, tmp = nan_helper(A_T)
A_T[nans] = np.interp(tmp(nans), tmp(~nans),A_T[~nans])
#A_norm = stats.zscore(A_T,axis=0,ddof=1)
mask = ~np.isnan(y0)
#y0 = [tmp[0] for tmp in y]
#w= linalg.lstsq(A_mat.T,y0)[0] 
w= linalg.lstsq(A_T[mask],y0[mask])[0]
# plotting the line
line = np.matmul(A_T[mask], w) # regression line
r2_scr = r2_score(y0[mask], line)

#plt.plot(A_oneVect,line,'r-',A_oneVect,y'o')
#plt.xlabel('Total Overdose Deaths')
#plt.ylabel('Civilian labor force')
#plt.show()
print(w)
print(r2_scr)

plt.plot(y0[mask],line,'bo',[0, 100],[0, 100],'r-')
plt.xlabel('True')
plt.ylabel('Predicted')
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.x

#index = [  6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71,  76, 81,\
#                                   87,  93,  99, 104, 109, 114, 119, 124, 129, 134, 139, 144, 149, \
#                                   154, 159, 164, 169, 174, 179, 184, 189, 194, 199, 204, 209, 214, \
#                                   219, 224, 234, 239, 244, 249, 254, 259, 265, 270, 275, 280, 285, \
#                                   290, 295, 302, 307, 311, 316, 321, 326, 331, 336, 341, 346, 351, 0]
#above are 2017


w_norm = stats.zscore(w)
high_weight_ixs = np.abs(w_norm)>0.25
plt.plot(w,'o')

val_vec = [index[i] for i in range(len(high_weight_ixs)) if high_weight_ixs[i]==1]
val_weights = [w[i] for i in range(len(high_weight_ixs)) if high_weight_ixs[i]==1]
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

