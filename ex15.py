# coding=utf-8
from sys import argv # import a module called argv

script, file_name=argv # unpack

txt=open(file_name) # open file and save the option
print("Here's your file %r:\n"% file_name) # print the file name.
print(txt.read()) # read the file and print the content which inside the file
#
#print("Please type the file name again.") # recommend user type the file name again.
#file=input(">") # input the file name
#print("\n") # add a new line
#
#txt=open(file) # open the file and save the option
#print(txt.read()) # print the content which inside the file.
txt.close()

