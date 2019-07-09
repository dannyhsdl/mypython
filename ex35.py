# coding= utf-8

from sys import exit

# Enter Gold room
def gold_room():
    print("This room is full of gold. How much do yo take?")
    
    next=input(">")
    if "0" in next or "1" in next:
        how_much= int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much<50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# Enter bear_room
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved=False

    while True:
        next=input(">")

        if next=="take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next=="taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")   
            bear_moved=True
        elif next=="taunt" and bear_moved:
            dead("The bear gets pissed off and chews your lag off.")
        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print("I got to idea what that means.")

# Enter Cthulhu room
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next=input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# You are dead
def dead(why):
    print(why,"Good job!")
    exit(0)

# Get to started
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do yo take?")

    next=input(">")
    
    if next=="left": # type "left", enter Bear room
        bear_room()
    elif next == "right": # type "right",enter Cthulhu room
        cthulhu_room()
    else:
        dead("You stumble around the the room until you starve.")
start() # star game