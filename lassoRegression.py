import util
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso #LassoCV
from sklearn.preprocessing import StandardScaler
import pdb

scaler = StandardScaler()
gen_func = util.generate_A_and_b()
A, y = gen_func.generate()

A_mat = np.asarray(scaler.fit_transform(A))
y0 = y[0]

lasso = Lasso(alpha=0.3)
lasso.fit(A_mat.T,y0)
# clf = LassoCV()
#
# sfm = SelectFromModel(clf, threshold=0.01)
# A_mat = np.asarray(A)
# sfm.fit(A_mat.T,y[0])
# n_features = sfm.transform(A).shape[1]
#
# while n_features > 10:
#     sfm.threshold += 0.1
#     A_transform = sfm.transform(A)
#     n_features = A_transform.shape[1]
pdb.set_trace()
