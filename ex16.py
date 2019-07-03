# coding=utf-8
# what this program do is to creat a text file and write something into it just like we do it directly
# But here we do it by a program (or codes)
# So,let's get started.

from sys import argv # import argv module
script,filename=argv #unpack Two arguments one is script name the another is file name.
print("We're going to erase %r."% filename) # print the name of the file.
print("If you don't want that,hit Ctrl-C(^C).") # you can type Ctrl-C to stop the procedur
print("If you do want taht, hit RETURN.") # recomemd you to type RETURN if want to continue

input("?") # here you can type Ctrl-C or RETURN, it's up to you.

print("Opening the file...") # recomemd you that the program s opening the file.
target= open(filename,'w') # this is a opreation to open the file by writing. And then save the option

print("Truncating the file. Goodbye!")
target.truncate() # no return value

print("Now I'm going to ask you for three lines.") # recomemd you to input some information

line1= input("line 1: ") # this is a option, which means you gotta input something,then you input something
line2= input("line 2: ") # remember you do this thing in a terminal window, instead of a notebook.
line3= input("line 3: ") # by the way this option will be saved.

print("I am going to write these to the file.") # recomemd you that the program will write there stuff to 
# the file, just like you write it down on the notebook. Hopefully, the program helps you to write it to
# the file, not you

target.write(line1) # a option, which writes the stuff to the file.
target.write("\n") # return
target.write(line2) # here the same way
target.write("\n") # return
target.write(line3) # same way
target.write("\n") # return

print("And finally, we close it.") # the program recomemds you the file is gonna be closed
target.close() # close the file.

# it seems confusing,huh. But here I am gonna tell you the details.

# we imported a module call argv
# we created a script called ex16.py, and we created text file called test.txt(but there wassn't a file
# called test.txt) ex16.py and text.txt are 2 arguments which are invovel in the argv, import them to argv
# then unpack
# recomemd you erase the file.
# recomemd you that it's your choice to stop or continue(the procedur)
# type Ctrl-C to stop or RETURN to continue

# Open the file by writing, and then save it.
# Then truncating the file
# Ask you to input information
# ......
# Write the information to the file
# And finally, we close the file.
# So, this is the steps

# You can check the text file which in the floser