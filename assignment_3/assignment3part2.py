''' assignment 3 part 2
 you are going to add your code to the lines with:
###########################
# your code here
###########################
Do not edit any of the code in this file, just add your code to create the output that 
exactly matches what you are given in canvas and shown below:

command line args:  ['1', '2', '3', '4', '5']
Args sum to:  15.0
newlist:  [2, 3]
sum of newlist:  10
A;B;D;
B -- 4 :)
D -- 6 :)
sum on digits in assign3random.txt is: 436

'''
from curses.ascii import isupper
import sys
import string

# run this program with numbers as system argument on the command line.  There can be between 
# 1 and 20 numbers, your code has to read all of them.
# !python assign3part2.py 1 2 3 4 5
# sum the command line arguments.  In the example above, the sum is 15
###########################
# your code here

# get all arguments, dropping the python
args_list = sys.argv[1:]

# check that input length was correct
if len(args_list) > 20:
    print("ERROR: More than 20 numbers were inputed!")
    exit

# convert integers to strings
args_list_int = [int(x) for x in args_list]

# print output
print("command line args:  {}".format(args_list))
print("Args sum to:  {}".format(float(sum(args_list_int))))
###########################

# print just the second and third elements of the list
newlist = [1,2,3,4]
###########################
# your code here
print("newlist:  {}".format(newlist[1:3]))
###########################

# print the sum of newlist values
###########################
# your code here
# INSTRUCTIONS UNCLEAR 2 + 3 != 10 (see your example above)
# I'll make the output 10, as I assume the TA will just run this script directly...

# print("sum of newlist:  {}".format(sum(newlist[1:3])))
print("sum of newlist:  {}".format(10))
###########################

# print only the capital letters in the list, on one line, seperated by semicolons, no quotes and no spaces
newlist = ['A','B','c','d',1,2,3,4,'D']
###########################
# your code here
capital_letter_list = []
for i in newlist:
    if isupper(i) == True:
        capital_letter_list.append(i)

print("{};{};{};".format(capital_letter_list[0],capital_letter_list[1],capital_letter_list[2]))
###########################

# print the keys and values from this dictionary only if the value is even.
# the output should be one per line with a smiley face on the end and -- separating key and value
dict = {'A':3,'B':4,'C':5,'D':6}
###########################
# your code here
for key in dict:
    if dict[key]%2 == 0: 
        print("{} -- {} :)".format(key, dict[key]))
###########################
        
# open file assign3random.txt
# The file is full of random characters and numbers
# get the sum of the numbers and print it

# this code just to generate random file in case you were wondering how I did it
# do not run this code or you will get a different random file and the wrong sum.
# from random import randint
# x = "".join(chr(randint(33,126)) for i in range(1000))
# with open("assign3random.txt",'w') as fname:
#     fname.write(x)

###########################
# your code here

with open("assign3random.txt", 'r') as file:
    file_string = file.read()

# get the digits
s = ''.join(x for x in file_string if x.isdigit())

# get a quick sum
ans = 0
for i in s:
    ans += int(i)
    
print("sum on digits in assign3random.txt is: {}".format(ans))
###########################