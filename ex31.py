# coding = utf-8
# asking people, and making decesions according to
# the answers which provided by your clients
print("Now, the 'play game' button is on the screen, type 'yes' to continue or 'no' to exit.")

type = input(">")
if type == "yes":
    print("The game is now on.")
    print("You enter a dark room with 2 doors. Do you go through door #1 or door #2?")

    door = input(">")

    if door == "1":
        print("There's a gaint bear eating a cheese cake. What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")

        bear = input(">")

        if bear == "1":
            print("The bear eats your face off. Good job!")
        elif bear == "2":
            print("The bear eats your legs off. Good job!")
        else:
            print("Well, doing %s is probably better. Bear runs away."% bear)

    elif door == "2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries.")
        print("2. Yellow jaket clothespins.")
        print("3. Understanding revolvers yelling meoldies.")

        insanity = input(">")

        if insanity == "1" or insanity == "2":
            print("Your body servives powered by a mind of jello. Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck. Good job!")
    else:
        print("You stumble around and fall on a knife and die. Good job!")
elif type == "no":
    print("Ok, see you next time.")
else:
    print("Ooops, an error occured!")
