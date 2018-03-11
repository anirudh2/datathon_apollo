# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:34:19 2018

@author: lengchun
"""

import pylab
import util
import numpy as np
import matplotlib.pyplot as plt
import pdb

#gen_func = util.generate_A_and_b()
gen_func = util.generate_A_census()
A, y = gen_func.generate()

A = np.asarray(A)
A_oneVect = np.sum(A,1)
# pdb.set_trace()
pylab.plot(np.arange(2000,2000+len(A_oneVect),1),A_oneVect,'o')
pylab.show()
#
# plt.hist(A_oneVect)
# plt.title("Histogram")
# plt.xlabel("Housing")
# plt.ylabel("Frequency")
