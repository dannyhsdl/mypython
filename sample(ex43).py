# coding = utf - 8
import time
from random import randint
from random import sample

class Game(object):

    """Default function or methords it includes some positional arguments you need"""

    def __init__(self,names,jobs,salarys,passive_income,total_income,total_pay,net_cash,cash,my_passive,my_pay,cash_decrease,cash_increase):
        self.names = names
        self.jobs = jobs
        self.salary = salary
        self.passive_income = passive_income    # line 11
        self.total_income = total_income    # line 12
        self.total_pay = total_pay
        self.net_cash = self.total_income - self.total_pay    # line 14
        self.cash = cash
        self.my_passive = my_passive
        self.my_pay = my_pay
        self.cash_decrese = cash_decrease
        self.cash_increase = cash_increase


    def person_info(self):

        """print your personal imformation"""

        a = sample(self.names,1)[0]
        b = sample(self.jobs,1)[0]
        print("Loading your personal information...\n")
        time.sleep(3)
        #print("""
        #     Your name: %s. You are %s. Your basic salary is %d dollars
        #    Your passive income: %d dollars   Total income: %d dollars
        # Total pay: %d dollars    Net cash : %d dollars
        #  """%(a,b,self.salary,self.my_passive,self.total_income,self.total_pay,self.net_cash))
        person_details = {"Your name":a,"Your job":b,"Basic salary":self.salary,
                          "Passive income":self.my_passive,"Total income":self.total_income,
                          "Total pay":self.total_pay,"Net cash":self.net_cash}
        for i,k in person_details.items():
            print("\t",i,":",k)

    def cash_decrease(self):

        """You cash will decrease if you buy something buy cash"""

        print("Your cash reduced.")
        a = self.cash_decrease
        b = 0
        if a == 500:
            print("Buy gold,cost %d dollars"% a)
            cash_cost = b - a
            print("Refreshing your account...")
            time.sleep(3)
            return cash_cost
        elif a == 20:
            print("Stock opportunity: MYT4U %d dollars"% a)
            choose = input("Do you wanna buy:(y/n) ")
            if choose == "y":
                number = int(input("How many do you want: "))
                cash_cost = b-a*number
                print("Refreshing your account...")
                time.sleep(3)
                return cash_cost
            else:
                Game.runner(self)
        elif a == 30:
            print("Stock market: on2u %d dollars"% a)
            choose = input("Do you wanna buy?(y/n) ")
            if choose == "y":
                number = int(input("How many do you want: "))
                cash_cost = b-a*number
                print("Refreshing your account...")
                time.sleep(3)
                return cash_cost
            else:
                Game.runner(self)
        elif a == 200:
            print("Join a party, cost %d dollars"% a)
            choose = input("Do you wanna join the party:(y/n) ")
            if choose == "y":
                cash_cost = b-a
                print("Changing your account...")
                return cash_cost
            else:
                Game.runner(self)

    def cash_increase(self):

        """ your cash increase if you get paycheck or sell a house or sell stock tickets"""

        print("Add your cash:")
        print("You sell something.")
        a = self.cash_increase
        b=0
        if a == 380:
            print("You get paycheck: %d dollars"% a)
            cash_get = b+a
            print("updating your account...")
            time.sleep(3)
            return cash_get
        elif a == 3020:    # line 85
            print("You get paycheck: %d dollars"% a)
            cash_get = b+a
            print("Updating your account...")
            time.sleep(3)
            return cash_get
        elif a == 1700:
            print("You get paycheck: %d dollars"% a)
            cash_get = b+a
            print("Updating your account...")
            time.sleep(3)
            return cash_get
        elif a == 1500:
            print("You get paycheck: %d dollars"% a)
            cash_get = b+a
            print("Updating your account...")
            time.sleep(3)
            return cash_get

    def passive_income(self):
       
        """ You get or lose passive income
            You get get passive income if you 
            buy a house for lease,or you creat a
            company or join a company which gives you money"""

        print("You get or lose passive income.")
        b = 0
        c = int(sample(self.passive_income,1)[0])
        if c == 100:    # line 107
            print("You buy a house: you got %d dollars"% c)
            passive_come = b+c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_come
        if c == 950:
            print("You sell a house,lose %d dollars"% c)
            passive_income = b - c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_income
        elif c == 1700:
            print("You bought a house,You got %d dollars"% c)
            passive_come = b+c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_come
        elif c == 400:
            print("You sell a house,lose %d dollars"% c)
            passive_income = b - c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_income
        elif c == 800:
            print("You bought a house,You got %d dollars"% c)
            passive_come = b+c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_come
        elif c == 2000:
            print("You bought a house,You got %d dollars"% c)
            passive_come = b+c
            print("Refreshing your account...")
            time.sleep(3)
            return passive_come
    def month_pay(self):

        """ Your pay out details very month,it gets money out 
            of your pocket, your pay out adding,for example,
            take loan from a bank, chirldren supports, house
            rent and etc,but your pay will down if return loan"""

        print("Pay for something you need every month.")
        e = 0
        f = int(sample(self.my_pay,1)[0])
        if f == 250:
            print("Truck fix every month: %d dollars"% f)
            pay = e + f
            print("refreshing your account...")    # 150
            time.sleep(3)
            return pay
        elif f == 170:
            print("For chirld support: %d dollars"% f)
            pay = e + f
            print("refreshing your account...")    # line 156
            time.sleep(3)
            return pay
        elif f == 200:
            print("Properties care: %d dollars"% f)
            pay = e + f
            print("refreshing your account...") # line 162
            time.sleep(3)
            return pay
        elif f == 100:
            print("Car care: %d dollars"% f)
            pay = e + f
            print("refreshing your account...") # line 168
            time.sleep(3)
            return pay
        elif f == 30:
            print("For phone realese: %d dollars"% f)
            pay = e + f
            print("refreshing your account...")    # line 174
            time.sleep(3)
            return pay
        elif f == 150:
            print("Protect house: %d dollars"% f)
            pay = e + f
            print("refreshing your account...")    # line 180
            time.sleep(3)
            return pay
        elif f == 50:
            print("Return loan: %d dollars"% f)
            pay = e - f
            print("updating your account...")
            time.sleep(3)
            return pay
        elif f == 60:
            print("Return education loan: %d dollars"% f)
            pay = e - f
            print("Updating your account...")
            time.sleep(3)
            return pay
        elif f == 340:
            print("Return loan for a boat: %d dollars"% f)
            pay = e - f
            print("Updating your account...")
            time.sleep(3)
            return pay
    # def net_cash(self):
    def room_101(self):
    
        passive_income = self.my_passive    # line 186
        total_pay = self.total_pay
        cash = self.cash
        total_income = self.total_income
        functions = [Game.cash_decrease,Game.cash_increase,Game.month_pay,Game.passive_income]
        while passive_income < total_pay:    # line 190
            Random_f = sample(functions,1)[0]
            if Random_f == Game.passive_income:
                passive_income = passive_income + Game.passive_income(self)
                print("Your passive income is now: %d dollars"% passive_income)
                print("\n")
            elif Random_f == Game.month_pay:
                total_pay = total_pay + Game.month_pay(self) # new line 192
                print("Your total pay is now: %d dollars"% total_pay)
                print("\n")
            
            else:
                Random_f(self)
        print("Congratulations! You successfully finished it.")
        exit(0)

    def room_202(self):

        passive_income = self.my_passive    # line 186
        total_pay = self.total_pay
        cash = self.cash
        total_income = self.total_income
        functions = [Game.cash_decrease,Game.cash_increase,Game.month_pay,Game.passive_income]
        while passive_income < total_pay*2:    # line 190
            Random_f = sample(functions,1)[0]
            if Random_f == Game.passive_income:
                passive_income = passive_income + Game.passive_income(self)
                print("Your passive income is now: %d dollars"% passive_income)
                print("\n")
            elif Random_f == Game.month_pay:
                total_pay = total_pay + Game.month_pay(self) # new line 192
                twotime_pay = total_pay*2
                print("Your total pay is now: %d dollars"% total_pay)
                print("Your double total pay every month is: %d dollars"% twotime_pay)
                print("\n")
            
            else:
                Random_f(self)
        print("Congratulations! You successfully finished it.")
        exit(0)
        
        
    def runner(self):

        """Starting program, it is access to entire program"""

        print("Program is starting...")
        time.sleep(3)
        print("There are two rooms to enter to enter the game.")
        print("a. room 101  b.room 202")
        print("Make your own choice,the program will run automatically.")
        print("which one do you want?")
        choose = input("Your choice: (a/b) ")
        if choose == "a":
            print("Welcome to ROOM 101.")
            time.sleep(3)
            Game.room_101 (self)
        elif choose == "b":
            print("Welcome to ROOM 202.")
            print("In 202,your passive income must be doublu times than total_pay(or equals).")
            time.sleep(3)
            Game.room_202(self)
        else:
            print("Sorry,an error occured.Do you wanna try again?")
            choose = input("(y/n) ")
            if choose == "y":
                Game.runner(self)
            else:
                print("Ok,see you next time")
                exit(0)
 
""" Define real arguments"""
       
names = ["Lihua","Sam","Simon","Amy"] 
jobs = ["police",'soilder',"chief","programmer","farmer","driver","director","doctor"]
salary = randint(5000,10000)
passive_income = [100,950,1700,400,800,2000]
my_passive = 0
total_income = salary + my_passive
total_pay = randint(1000,5000)
net_cash = total_income - total_pay
cash = randint(5000,10000)
my_pay = [250,170,200,100,30,150,50,60,340]
cash_decrease0 = [500,20,30,200]
cash_decrease = int(sample(cash_decrease0,1)[0])
cash_increase0 = [320,3020,1700,1500]
cash_increase = int(sample(cash_increase0,1)[0])

"""Give the real arguments to the class
    and call major methords(or functions) which are included in the class"""

a = Game(names,jobs,salary,passive_income,total_income,total_pay,net_cash,cash,my_passive,my_pay,cash_decrease,cash_increase)
a.person_info()
print("\n")
a.runner()

# In this program,I used class,functions,for-loop
# and while-loop, lists, dicts and so on.
# Passive income is bigger or equrals than total
# pay(or double total pay) is the key to finish the program
# Some times,we quit the program in no time if net flow is
# less than zero.
# Maybe there are some problems I didn't find out.
# I'd appreciate it if you leave a comment on my project
# Thanks a lot
               
        