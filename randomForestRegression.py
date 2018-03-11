from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
import util
import numpy as np
import pdb

scaler = StandardScaler()
gen_func = util.generate_A_and_b()
A, y = gen_func.generate()

A_mat = np.asarray(scaler.fit_transform(A))
y0 = y[0]


model = RandomForestRegressor(n_estimators=100, oob_score=True, random_state = 42)
model.fit(A_mat.T,y0)
pdb.set_trace()
print("AUC - ROC : ", roc_auc_score(y0,model.oob_prediction_))
