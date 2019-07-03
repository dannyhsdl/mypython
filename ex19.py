# coding=utf-8
# first we difine a function

def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print("You have %d cheeses."% cheese_count)
    print("You have %d boxes of crackers!"% boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# and second, we call the function
# 1st methord GIVE THE FUNCTION VALUE DIRECTLY

print("We can just give the function numbers directly.")
cheese_and_crackers(20,30) # call function and give it the values

# 2nd methord GIVE THE FUNCTION VALUES FROM OUR SCRIPT

print("Or,we can use variable from our script:")
amount_of_cheese= 10 # give a value to the variable
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# 3rd methord DO MATH INSIDE THE FUNCTION

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6) # do math inside the quetes

# 4th methord COMBINE VARIABLES AND MATH

print("And we can combine the two,variables and math:") # combie variables and math

cheese_and_crackers(amount_of_cheese+100, # run function cheese_and_crackers
amount_of_crackers+1000)