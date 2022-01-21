"""
# Class: COMP 3006
# Author: Brian Miller
# DU ID: 873601817
# Date: 1/20/2021
# Github Repo: https://github.com/BrianMillerS/DU_COMP3006

## DESCRIPTION ##
# This script takes in at least one txt file and generates a csv file with the letter counts from
# the txt files. Various parameters are avilable to the user to customize their letter counting
# experience.

## DEPENDENCIES ##
# txt files have one line, no "\n" at the end
# the arguments for the script are supplied in the order demonstrated -c -l -z
# the letters after -l, are in lowercase

## USAGE ##
# python3 count.py [-c] [-l letters] [-z] file_1 file_2 ... file_n
# -c :: an optional flag that distinguishes between upper and lower case. For example, the file 'aA' would count one 'a' and one 'A'.
# -l :: an optional flag with an argument, that only prints out the frequencies of the characters in the argument letters. For example, '-l aeiou' counts only vowels.
# -z :: an optional flag that prints a row for every character, even when it occurs zero times.

## NOTES TO THE GRADER ##
In the edge case that -l and -z are both used, -l 'overrides' -z, and only the letter from the 
-l argument are returned. The instructions did not cover this directly, but I assumed this was
proper solution as the word 'only' is used in the explanation of the -l argument 
('... only prints out the frequencies of the characters in the argument letters.').

Additionally, the assignment said the supply add_frequencies() with an empty dictionary
(at least for the first file). When I wrote out my logic/ pseudocode, propogating a dict 
with counts of zero for the letters to be counted seemed like the more traightforward approach. 
Slightly different approach, same result. 
"""


import sys
import string


def add_frequencies(d, file, remove_case):
    """[summary]
    Propogates the dictionay 'd' with letter counts from a single txt file.
    Returns an updated version of 'd' with the added counts.

    Args:
        d ([dict]): [dictionary with keys as letters, and values as integers]
        file ([str]): [file name to search]
        remove_case ([bool]): [True: case is ignored, all letters are counted as lower case
        False: case is used, letters are counted according to their case]
    """
    # open the file
    with open(file) as f:
        file_string = f.readlines()[0]
    
    # check if the -c option is in place, if so, change all letters to lower case
    if remove_case == True:
        file_string = file_string.lower()
    
    # perform the counting
    for i in file_string:  # for every element in the string (aka, the single line txt file)
        if i in d.keys():  # if the letter should be counted
            d[i] = d[i] + 1  # update the dict
    
    return(d)
    

if __name__ == "__main__":
    
    ## Process script arguments ##
    args = sys.argv[1:]  # get all arguments
    
    # -c argument
    if '-c' in args:
        c_arg_supplied = True
        args = args[1:]  # drop the -c from the list of args
    else:
        c_arg_supplied = False
        
    # -l argument
    if '-l' in args:
        l_arg_supplied = True
        l_arg_letters = args[1]  # extract the letters from the -l argument
        args = args[2:]  # drop the -l and letters from the list of args
    else:
        l_arg_supplied = False
    
    # -z argument
    if '-z' in args:
        z_arg_supplied = True
        args = args[1:]  # drop the -z from the list of args
    else:
        z_arg_supplied = False
    
    # the remaining arguments are the text file(s)
    txt_files = args
    
    ## Create dictionary to propogate ##
    # if -l, then make dict of just those letters
    if l_arg_supplied == True:
        d = dict.fromkeys(list(l_arg_letters), 0)
    else:
        d = dict.fromkeys(list(string.ascii_lowercase), 0)

    # if -c, then add upper case letters to dict
    if c_arg_supplied == True:
        l_arg_letters_upper = [letter.upper() for letter in d.keys()]  # get the uppercase versions of the letters
        d_to_merge = dict.fromkeys(list(l_arg_letters_upper), 0)  # make a separate dict with those upper case letters
        
        # merge the two upper and lowercase dicts
        d3 = d.copy()  # copy the original
        d3.update(d_to_merge)  # add the new uppercase letters
        d = d3  # update d as the newly merged dict
    
    ## Perform Counting ##
    for txt_file in txt_files:  # for every file supplied
        d = add_frequencies(d, file = txt_file, remove_case = not c_arg_supplied)  # update d with the additional counts

    ## If -z is not used, drop all letters with zero counts ##
    if z_arg_supplied == True:
        pass
    else:
        d = {x:y for x,y in d.items() if y!=0}  # drop letters with zero counts
    
    ## Print Results ##
    for key in d.keys():
        print('"{}",{}'.format(key, d[key]))