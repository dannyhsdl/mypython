#coding=utf-8
# The name 'Zed A. Shaw' behind the '=' is format string.

my_name = 'Zed A. Shaw'
my_age = 35 # Not a lie
my_height = 74 # Inches
my_weight = 180 # lbs

my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s."% my_name)# '%s' refers to content which was invovled in the format string.

print("He's %d inches tall."% my_height)# '%d' here refers to number.
print("He's %d pounds heavey."% my_weight)
print("Actually that's not too heavy.")

print("He's got %s eyes and %s hair."%(my_eyes,my_hair))

print("His teeth are usually %s depending on the coffee."% my_teeth)

# This line is tricky, try to get it exactly right

print("If I add %d,%d,and %d I get %d."% (my_age,my_height,my_weight,my_age+my_height+my_weight))
# '%r' refers to whatever you want to print.
print("My name is %r,and I have %r eyes and %r teeth and %r hair.Nice to meet you."%(my_name,my_eyes,my_teeth,my_hair))