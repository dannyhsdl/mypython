# coding = utf-8
people = 30
cars = 40
buses = 15

if cars > people: # if cars greater than  people
    print("We should take the cars.") # Then print this

elif cars < people: # if cars less than people
    print("We should not take the cars.") # then print this.

else: # neither they do 
    print("We can't decide.") # then pint this

if buses > cars: # if buses greater than cars
    print("That's too many buses.") # then print this

elif buses < cars: # if buses less than cars
    print("Maybe we should take the buses.") # then print this

else: # neither they do
    print("We still can't decide.") # then print this

if people > buses: # if people greater then buses
    print("Alright,let's just take the buses.") # then print this

else: # neither they do
    print("Fine,let's stay home then.") # then print this

if cars > people and buses < cars:
    print("We can take the cars.")

if people > cars or cars < buses:
    print("We can make a choice.")