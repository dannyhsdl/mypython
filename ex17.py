# coding = utf-8
# This is a script called ex17.py
# What it used for: Copying contents in a file to another file.
from sys import argv
from os.path import exists # Here import a module called exists, it 
# returen a value (True/False)
# import is very important stuff.

script,from_file,to_file=argv

print("Copying from %s to %s."% (from_file,to_file))

# we could do this on 1 line too,how?
input_file=open(from_file)
indata= input_file.read()

print("The input file is %d bytes long"% len(indata))

print("Dose the output file exist? %r"% exists(to_file))
print("Ready,hit RETURN to continue,Ctrl_c to abort.")

input()

output= open(to_file,'w')
output.write(indata)

print("Alright, all done.")

output.close()
input_file.close()