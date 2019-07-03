#coding=utf-8
# You gotta add the stuff like in line 1 if you are in another country where people don't
#speak English, But it is not necessary in all countries around the world.
# So, we gotta know something before we go.
# '%r' means you can print whatever you want to print.
# '%d' mean you can print a number.
# And '%s' means you can print the content which is invoveled in a string.
# So, let'get started.

formatter="%r %r %r %r"

print(formatter %(1,2,3,4))
print(formatter %("one","two","three","four"))
print(formatter %(True,False,False,True))
print(formatter %(formatter,formatter,formatter,formatter))
print(formatter%(
    "I had this thing.",
    "That you could type up toght.",
    "But it didn't say.",
    "So, I said goodnight.")
       )
# Let's take a look at the result. Thing's gonna be interesting.