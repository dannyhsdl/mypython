#coding=utf-8
print("How old are you?",) # Do you know what the comma here use for?
age= input()

print("How tall are you?",)
height= input()

print("How much do weight?",)
weight= input()

print("So,you are %r old,%r tall and %r heavy."%(age,height,weight)) # notice the format strings here.

# let's do something else.
print("\n")
print("#"*10)
print("Here are some question below.")

print("Where are you from? ")
country= input()

print("What language do you speak? ")
language= input()

print("What do you do? ")
job= input()

print("So, you're from %s, you speak %s, and you are a %s."%(country,language,job))
print("Good job!")


