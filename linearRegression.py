# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:44:35 2018

@author: lengchun
"""

from numpy import arange,array,ones,linalg
from pylab import plot,show

import pdb
import build_dataset

parser = build_dataset.parse_args()
# pdb.set_trace()
args = parser.parse_args(['-f','data/','-c',[1,2,3]])
build_dataset.main(args)
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
