"""
# Class: COMP 3006
# Author: Brian Miller
# DU ID: 873601817
# Date: 1/31/2021
# Github Repo: https://github.com/BrianMillerS/DU_COMP3006

This script takes in at least one txt file and generates a csv file with the letter counts from
the txt files. Various parameters are avilable to the user to customize their letter counting
experience.

## DEPENDENCIES ##
The arguments for the script are supplied in the order demonstrated -c -l -z
The letters after -l, are in lowercase

## USAGE ##
# python3 count.py [-c] [-l letters] [-z] file_1.txt file_2.txt... output_file.csv
# -c :: an optional flag that distinguishes between upper and lower case. For example, the file 'aA' would count one 'a' and one 'A'.
# -l :: an optional flag with an argument, that only prints out the frequencies of the characters in the argument letters. For example, '-l aeiou' counts only vowels.
# -z :: an optional flag that prints a row for every character, even when it occurs zero times.
"""

import sys
import csv
import string
from count import generate_count_csv, add_frequencies

# get the csv file (the last argument)
args = sys.argv[1:]  # get all arguments
output_filename = args[-1]

# perform counting
d = generate_count_csv()

# write the results to a csv file
with open(output_filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(d.keys(), d.values()))  # write keys and values from dict to csv as columns