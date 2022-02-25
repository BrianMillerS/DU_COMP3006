#!/usr/bin/env python3
# Author: Brian Miller
# DU ID: 873601817
# Date: 02/24/2022


import numpy as np
import pandas as pd
import csv
import statistics
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)

#### PART 1 ####----------------------------------------------
print("\nPART 1 OUTPUT:")

# define matrix params
matrix_low = 1
matrix_high = 420
matrix_n_rows = 1000
matrix_n_cols = 10
matrix_col_names = ['bob','bobby','bobs','bobino','bobtube','bobsicle','bobslob','bobboy','bobb','bobtacular']

# make the matrix
bob_matrix_np = np.random.randint(low = matrix_low, high = matrix_high, size=(matrix_n_rows, matrix_n_cols))
print("matrix generated...")
print("This matrix consists of random integers from 1 to 420")

# write the matrix to csv
output_file_name = 'bob_matrix.csv'

with open(output_file_name, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(matrix_col_names) 
        
    # writing the data rows 
    csvwriter.writerows(bob_matrix_np)

#### PART 2 ####----------------------------------------------
bob_matrix_pd = pd.read_csv(output_file_name)

# check that the data was loaded correctly
print("\nPART 2 OUTPUT:")
print("Matrix (rows, cols): {}".format(bob_matrix_pd.shape))
print("Matrix columns: {}".format(list(bob_matrix_pd.columns)))

#### PART 3 ####----------------------------------------------
print("\nPART 3 OUTPUT:")

# initiate empty output lists
means, stds, modes, medians = [],[],[],[]

# for each column, calculate statistics, add them to the lists
for column_name in bob_matrix_pd.columns:
    means.append(statistics.mean(bob_matrix_pd[column_name]))
    stds.append(statistics.stdev(bob_matrix_pd[column_name]))
    modes.append(statistics.mode(bob_matrix_pd[column_name]))
    medians.append(statistics.median(bob_matrix_pd[column_name]))

print("Calculations complete...")

#### PART 4 ####----------------------------------------------
print("\nPART 4 OUTPUT:")

print("writing to txt file...")

# open a file
txt_filename = "bob_matrix_statistics.txt"
f = open(txt_filename, "a")

# make a summary df with all the calculations
for i in range(0,10):
    f.write("\nColumn Name: {}\n".format(bob_matrix_pd.columns[i]))
    f.write("Mean: {}\n".format(means[i]))
    f.write("Std: {}\n".format(stds[i]))
    f.write("mode: {}\n".format(modes[i]))
    f.write("Median: {}\n".format(medians[i]))

# display the column names
f.write("\nColumn Names:\n")
f.write(str(list(bob_matrix_pd.columns)))

# display a sample of the matrix
f.write("\n\nThree row sample (first 3 rows):\n")
f.write(str(bob_matrix_pd.iloc[0].values.tolist()))
f.write("\n")
f.write(str(bob_matrix_pd.iloc[1].values.tolist()))
f.write("\n")
f.write(str(bob_matrix_pd.iloc[2].values.tolist()))

# close the file
f.close()