# coding = utf-8
list0=['copied.txt','ex15_sample.txt']
list1=['test.txt','test1.txt']
list2=['myfile0.txt','hello.py.txt']
text_doc=list0+list1+list2
"""for each in text_doc:
   you=input("Please input your file name: ")
   if you in text_doc:
       file_name=open(you,'r')
       print(file_name.read())
       file_name.close()
       choice=input("Do you wanna continue?(y/n) ")
       if choice == "y":
           you=input("input file name: ")
           file=open(you,'r')
           print(file.read())
           file.close()
       else:
           break
   else:
       remind=input("Oh, sorry, We can't find the file. Do you mind if we ask you input again(y/n)?")
       if remind == "y":
           print("Ok, here are some files available to search.")
           for file in text_doc:
               print("\t%s"% file)
           print("which one do you like to read?(input a number) your choice: ")
           you_choice=input(">")
           you_choice0=text_doc[int(you_choice)-1]
           file_again=open(you_choice0,'r')
           print("Contents in the file below:\n","please wait seconds")
           print(file_again.read())
           file_again.close()
       else:
           break"""
def open_file(n):
    i=0
    while i < 6:
        you = input("Please input the file name: ")
        if you in n:
            print("Ok, we open the file and show you the contents.")
            file=open(you,'r')
            print(file.read())
            file.close()
            you=input("Do you wanna open the next file or all files?(n/a) ")
            if you == "n":
                open_file(n)
            elif you == "a":
                open_all_files(text_doc)
                break
        else:    
            print("Sorry, we can not find the file.\n")
            choice=input("Do you wanna try again? (y/n) ")
            if choice=="y":
                open_file(n)
                break
            else: 
                break
        
def open_all_files(n):
    for items in n:
        print("\nThe contents in the file below:\n".upper())
        file=open(items,'r')
        print(file.read())
        file.close()

open_file(text_doc)

            