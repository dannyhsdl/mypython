#coding=utf-8
# '\n' is back-splash n,means return, you can add a new line by '\n' in a program
# '\' back-splash, escape sequences
#'\\' double back-splash
# let's do some practices,so that you will know what they mean.
# I'll show you some stuff here. Take a look at the 2 lines below.
# 1. " I am 6'2\" tall. "
# 2. ' I am 6\'2" tall. '

# so, lets get started.
# ' """ ' triple-quetes

tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# let me show you something else.
print("*"*10)

Mine='''
Big countrie:\n
\t* Russia
\t* Canada
\t* China
\t* America
\t* Austrilia\n\t* South Africa
'''
print(Mine)
# See, /'''/ and /"""/ are same way. \t means space.
# Let's take a look at the format strings and the escape sequences.
# format strings: %r, %s, %d,etc. escape sequences: \n, \, \\, \', \"",etc.

a="Russia"
b="Canada"
c="China"
d="America"
e="Austrilia"
f="South Africa"
print("This is %r."% a)
print('\'%r\' is the biggest country in the world by total area.'% a)
print("This is %s."% b)
print("This is \"%s\"."% c)
print('This is \'%s\'.'% d)
print("There are two countries:\n\t*\"%s\"\n\t*%r"%(e,f))
