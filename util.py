import pdb
import build_dataset


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
        cols_per_file_to_read = ['[6, 21]']
        num_cols_per_file = [2]
        A = []
        for file_num in range(len(files_to_read)):
            args = parser.parse_args(['--filename',files_to_read[file_num],'--columns_to_read',cols_per_file_to_read[file_num]])
            A_new = build_dataset.main(args)
            num_cols = num_cols_per_file[file_num]
            if file_num == 0:
                 A = A_new
            else:
                for i in range(num_cols):
                    A.append(A_new[i])

        # pdb.set_trace()

        # This gives us the full b-vector

        # args = parser.parse_args(['--filename',B_VEC_FILE_NAME,'--columns_to_read',B_VEC_COL_NUM_AS_A_STRING_LIST) #see cols_per_file_to_read
        # b = build_dataset.main(args)

        # pdb.set_trace()
        return A#, b
