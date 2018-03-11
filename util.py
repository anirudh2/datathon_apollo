import pdb
import build_dataset
import build_dataset_census
import build_dataset_overdose

class generate_A_and_b():

    def __init__(self):
        self.parser = build_dataset.parse_args()

    def generate(self):
        # How to pass arguments to build_dataset.py
        parser = self.parser
        # args = parser.parse_args([])
        # build_dataset.main(args)

        # This gives us the full A matrix
        files_to_read = ['data/2017CHR_CSV_Analytic_Data.csv']
        cols_per_file_to_read = ['[  6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71,  76, 81,\
                                   87,  93,  99, 104, 109, 114, 119, 124, 129, 134, 139, 144, 149, \
                                   154, 159, 164, 169, 174, 179, 184, 189, 194, 199, 204, 209, 214, \
                                   219, 224, 234, 239, 244, 249, 254, 259, 265, 270, 275, 280, 285, \
                                   290, 295, 302, 307, 311, 316, 321, 326, 331, 336, 341, 346, 351]']
        num_cols_per_file = [2]
        A = []
        for file_num in range(len(files_to_read)):
            args = parser.parse_args(['--filename',files_to_read[file_num],'--columns_to_read',cols_per_file_to_read[file_num],'--is_b_vec','False'])
            A_new = build_dataset.main(args)
            num_cols = num_cols_per_file[file_num]
            if file_num == 0:
                 A = A_new
            else:
                for i in range(num_cols):
                    A.append(A_new[i])

        # pdb.set_trace()

        # This gives us the full b-vector

        args = parser.parse_args(['--filename','data/2017CHR_CSV_Analytic_Data.csv','--columns_to_read','[229]','--is_b_vec','False']) #see cols_per_file_to_read
        y = build_dataset.main(args)

        # pdb.set_trace()
        return A, y

class generate_A_census_timeSer():

    def __init__(self):
        self.parser = build_dataset_census.parse_args()

    def generate(self):
       # How to pass arguments to build_dataset_census.py
        parser = self.parser

        # This gives us the full A matrix
        files_to_read = ['data/CLF01.xls']
        cols_per_file_to_read = ['[ 3,  7, 11, 15, 19, 23, 27, 31, 35, 39]']
        num_cols_per_file = [10]
        work_sheet_to_read = ['Sheet2']
        A = []
        for file_num in range(len(files_to_read)):
            args = parser.parse_args(['--filename',files_to_read[file_num],'--columns_to_read',cols_per_file_to_read[file_num],'--is_b_vec','False','--work_sheet_to_read',work_sheet_to_read[file_num]])
            A_new = build_dataset_census.main(args)
            num_cols = num_cols_per_file[file_num]
            if file_num == 0:
                 A = A_new
            else:
                for i in range(num_cols):
                    A.append(A_new[i])

        # pdb.set_trace()

        # This gives us the full b-vector

        work_sheet_to_read = ['online']
        args = parser.parse_args(['--filename','data/overdose_data_1999-2015.xlsx','--columns_to_read','[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]','--is_b_vec','True','--work_sheet_to_read',work_sheet_to_read[file_num]]) #see cols_per_file_to_read
        y = build_dataset_overdose.main(args)

        # pdb.set_trace()
        return A, y

