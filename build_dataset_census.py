# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:58:30 2018

@author: lengchun
"""

import pandas as pd
import numpy as np
import random
import os
import argparse
import sys
import ast

import pdb


# Check if a string represents an int
def repsInt(test_str):
    try:
        int(test_str)
        return True
    except ValueError:
        return False
def parse_args():
    # Create parser and add an argument to specify which directory the data is in
    roi = np.arange(3, 40, 4)
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-f','--filename', default='data/HSG/HSG01.xls',help="Dataset spreadsheet", required=False)
    parser.add_argument('-c','--columns_to_read', default= '[ 3,  7, 11, 15, 19, 23, 27, 31, 35, 39]' ,help="Which columns to read from the spreadsheet", required=False)
    parser.add_argument('-b','--is_b_vec', default='True',help="Are we trying to find the b vector", required=False)
    parser.add_argument('-w','--work_sheet_to_read', default='HSG01A',help="worksheet", required=False)
    return parser

def main(args):
    # Check if dataset is where we expect it to be
    # pdb.set_trace()
    assert os.path.isfile(args.filename), "Couldn't find the dataset at {}".format(args.filename)
    filename = args.filename
    all_columns = ast.literal_eval(args.columns_to_read)
    # Read data from speadsheet
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        df = pd.read_excel(filename, sheetname=args.work_sheet_to_read)
    elif filename.endswith('.csv'):
        df = pd.read_csv(filename)

    # Convert from pandas to numpy array
    full_array = df.values
    array_size = full_array.shape
    A = []
    # Use later to figure out if we want to
    first_data_ix = 100000
    if args.is_b_vec == "False":
        # Loop over rows of the full array
        for i in range(0,array_size[0]):
                if (repsInt(full_array[i,1])):

                    # if the 2nd column (country code) is 0, we are looking at a number for a
                    # state. This is what we want. Is this the case in other datasets?
                    if (int(full_array[i,1]) % 1000 == 0) and (full_array[i,1] > 0):
                        for col_num in range(len(all_columns)):
                            col = all_columns[col_num]
                            # Check if the data is a string. If not, write directly to temp (assumes a float)
                            if (type(full_array[i,col]) is str):
                                temp_str = full_array[i,col]
                                # The data has commas. Remove to cast to float
                                try:
                                    temp = float(temp_str.replace(',',''))
                                except AttributeError:
                                    print('Trying to use replace on temp_str when it is not a str')
                                    pdb.set_trace()
                            else:
                                temp = float(full_array[i,col])
                            # Make a new row in our A matrix if we are in the first entry
                            # Else add to existing rows
                            if not A or (i == first_data_ix):
                                A.append([temp])
                                first_data_ix = i
                            else:
                                A[col_num].append(temp)
    else:
        print('else')
        for i in range(0,array_size[0]):
            if i != 9:
                for col_num in range(len(all_columns)):
                    col = all_columns[col_num]
                    if (type(full_array[i,col]) is str):
                        temp_str = full_array[i,col]
                        # The data has commas. Remove to cast to float
                        try:
                            temp = float(temp_str.replace(',',''))
                        except AttributeError:
                            print('Trying to use replace on temp_str when it is not a str')
                            pdb.set_trace()
                    else:
                        temp = float(full_array[i,col])
                    # Make a new row in our A matrix if we are in the first entry
                    # Else add to existing rows
                    # pdb.set_trace()
                    if not A or (i == first_data_ix):
                        A.append([temp])
                        first_data_ix = i
                    else:
                        A[col_num].append(temp)

    # pdb.set_trace()
    return A



if __name__ == '__main__':
    parser = parse_args()
    args = parser.parse_args()

    main(args)
