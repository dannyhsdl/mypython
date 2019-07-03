# coding=utf-8
# Do you still remember what argv used for?
# let's take a look at how function related to files.
# the methords which used to print the contents which inside the file.

from sys import argv
script,input_file=argv

# creat the 1st function

def print_all(f):
    print(f.read()) # read file and then print it.(the whole of file)

# creat the 2nd function

def rewind(f): # move the point to the begining of the contents in the file
    f.seek(0) 

# creat the 3rd function

def print_a_line(line_count,f):
    print(line_count,f.readline()) # print each line which inside the file.(the part of the file)

# run functions

current_file=open(input_file) # open your file, and save the option

print("First let's print the whole file:\n")

print_all(current_file) # open the whole file by reading, and print the whole file.

print("Now let's rewind,kind of like a tape.")

rewind(current_file) # move the point to the begining of the contents in the file

print("Let's print 3 lines:") # what we do here is print contents in each line in the file

current_line=1
print_a_line(current_line,current_file) # print the contents in line 1 in the file

current_line =current_line+1
print_a_line(current_line,current_file) # print the contents in line 2 in the file

current_line+=1
print_a_line(current_line,current_file) # print the contents in line 3 in the file