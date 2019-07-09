# coding = utf-8
# Death note FBI

def start():
    print("Role:Light,Lewliet,Luke")
    print("Light:I'm justice,I'll find you and kill you,L!")
    print("Lawliet: II'm justice, I will catch you,Kira!")
    print("Luke:The human is interesting,Ha,Ha,Ha!")

def Capacity():
    print("Light: Ray,I'm Kira. Don't want to turn your haed.")
    print("Ray:!!!what do yo want to do?")
    print("""Light:watch up,take that book,
    write your collegues' name fallow the prompts""")
    while True:
        print("*"*10,"\t")
        name =input("")
        if name == "Ray":
            break
    print("."*10)
    print("Light:say goodbye to this world,Ray")
    print("The FBI all die from heart disease")
    print("Lawliet:......Kira......")

def justice_or_evil():
    print("FBI arrived in Japan, what Kira will do?")
    print("Luke:Someone behind us,yo should be careful")
    attitude=input("")
    if attitude =="yes":
        print("Light:Did you atart acting,L?")
        Capacity()
    else:
        die()

def die():
    print("""Luke: Light,You're lose, I will help you
    relief with DEATH NOTE, goodbye!""")

def meet():
    print("Lawliet:Welcome to join us!")
    print("Light: I'll try my best to catch Kira!")

def truth():
    print("Lawliet:Light...you..Kira.")
    print("Light: I win,L.")
    print("......After three days......")
    print("Light: that's right,I'm Kira,I'm dominate of the world.")
    print("Lawliet: You're crime,Kira.")
    print("Light:!!! L? !!!")
def final():
    print("Light: It's impossible.")
    print("Lawliet: You're note already changed by me.")
    print("Light: Luke,help me kill them, now!")
    die()
def start_game():
    start()
    Capacity()
    justice_or_evil()
    meet()
    truth()
    final()
start_game()