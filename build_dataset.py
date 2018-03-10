import pandas as pd
import numpy as np
import random
import os
import argparse

from tqdm import tqdm
import pdb

# Create parser and add an argument to specify which directory the data is in
parser = argparse.ArgumentParser()
parser.add_argument('--filename', default='data/2017CHR_CSV_Analytic_Data.csv',help="Dataset spreadsheet")
parser.add_argument('--columns_to_read', default=[0],help="Which columns to read from the spreadsheet")
if __name__ == '__main__':
    args = parser.parse_args()

    # Check if dataset is where we expect it to be
    assert os.path.isdir(args.filename), "Couldn't find the dataset at {}".format(args.filename)

    filename = args.filename
    # Read data from speadsheet
    if filename.endswith('.xls'):
        df = pd.read_excel(filename)
    elif filename.endswith('.csv'):
        df = pd.read_csv(filename)

    full_array = df.values
    array_size = full_array.shape
    A = []
    for i in range(2,array_size[0]):
        if int(full_array[i,2]) == 0:
            for col in args.columns_to_read:
                temp_str = full_array[i.col]
                temp = float(temp_str.replace(',',''))
                # A.append(temp)
                pdb.set_trace()

#     A = []
#
#         all_values = df.values
#         array_size = all_values.shape
#         premature_deaths = []
#         poor_mental_health_days = []
#         # pdb.set_trace()
#         # A = np.empty((0,51))
#         for i in range(1,array_size[0]):
#             if  int(all_values[i,2]) == 0:
#                 print(all_values[i,3])
#                 temp_str = all_values[i,6]
#                 temp = int(temp_str.replace(',',''))
#                 premature_deaths.append(temp)
#                 poor_mental_health_days.append(float(all_values[i,21]))
#
#         A = [premature_deaths]
#         A.append([poor_mental_health_days])
#         A = np.asarray(A)
#         pdb.set_trace()
# #
