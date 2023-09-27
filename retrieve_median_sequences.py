#!/bin/python3


import sys
import numpy as np
import pandas as pd

input_data = sys.argv[1]
output_data = sys.argv[2]

data = pd.read_csv(input_data, "\t")


##### Retrieve most abundant L1Md length from bed file

def most_frequent(lengths):
    return max(set(lengths), key = lengths.count)


line_lengths = list(data.iloc[0:, -1])
line_length_max = most_frequent(line_lengths) 

data_max = data[(data.iloc[0:, -1] >= (line_length_max - 10)) & (data.iloc[0:, -1] <= (line_length_max + 10))]


data_max.to_csv(output_data, "\t", index = False, header = None)
