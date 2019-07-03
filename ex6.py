#coding=utf-8
x= "There are %d types of people."% 10 #string 

binary= "binary"# string
do_not = "don't"# string

y="Those who know %s and those who %s." %(binary, do_not) # format string

print(x) # print string
print(y) # print string

print("I said: %r."%x) # print a string which contains the conten.
print("I also said: '%s'."%y) # print a string.

hilarious=False

joke_evaluation="Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious) # print it, '%r' refers to the whole conten.

w="This is the left side of..."
e="a string with a right side."

print(w+e) # Plus two strings, and then print it.