# Read Me
# Libraries Used: Python tabular:https://pypi.python.org/pypi/tabular/
# 1. Loops through each and every cell in the csv file. 
# 2. Finds whitespace only cells(data is not present in the cell but whitespace is present)
# 3. Prints the column name and the corresponding row no.

import csv
import tabular as tb

input_file = tb.tabarray(SVfile='sampledata.csv',verbosity=0,headerlines=1)
column_names = input_file.dtype.names

for column_name in column_names:
    row_no = 1
    for data_cell in input_file[column_name]:
        if str(data_cell).isspace():
            row_no += 1
            print 'Column Name:{0}, Row Number:{1} '.format(column_name, row_no)
        else:
            row_no += 1
