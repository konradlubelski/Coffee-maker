import sys

class CoffeeMachine():
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.cash = 550
        self.status = None 
        
    def choose_status(self):
        self.status = input("Write action (buy, fill, take, remaining, exit): ")
        print("")
        if self.status != "exit":
            if self.status == "buy":
                return self.choose_buy_action()
            elif self.status == "fill":
                return self.fill_action()
            elif self.status == "take":
                return self.take_action()
            elif self.status == "remaining":
                return self.remaining_action()
        if self.status == "exit":
            sys.exit()

    def choose_buy_action(self):
        self.kind_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu: ")
        print("")
        if self.kind_of_coffee == "1":
            return self.buy_action_espresso()
        elif self.kind_of_coffee == "2":
            return self.buy_action_latte()
        elif self.kind_of_coffee == "3":
            return self.buy_action_cappuccino()
        elif self.kind_of_coffee == "back":
            return self.choose_status()

    def buy_action_espresso(self):
        if (self.water >= 250 and self.milk >= 0 and self.coffee_beans >= 16 and self.disposable_cups >= 1):
            self.water -= 250
            self.coffee_beans -= 16
            self.disposable_cups -= 1
            self.cash += 4
            print("I have enough resources, making you a coffee!")
            print("")
        else:
            if self.water < 250:
                print("Sorry, not enough water!")
            if self.coffee_beans < 16:
                print("Sorry, not enough coffe beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")   
            
    
    def buy_action_cappuccino(self):
        if (self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1):
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.disposable_cups -= 1
            self.cash += 6
            print("I have enough resources, making you a coffee!")
            print("")
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            if self.milk < 100:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 12:
                print("Sorry, not enough coffe beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")   

    def buy_action_latte(self):
        if (self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1):
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.disposable_cups -= 1
            self.cash += 7
            print("I have enough resources, making you a coffee!")
            print("")
        else:
            if self.water < 350:
                print("Sorry, not enough water!")
            if self.milk < 75:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 20:
                print("Sorry, not enough coffe beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")   

    def fill_action(self):
        add_water = int(input("Write how many ml of water do you want to add: "))
        add_milk = int(input("Write how many ml of milk do you want to add: "))
        add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        add_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_coffee_beans
        self.disposable_cups += add_disposable_cups
        

    def take_action(self):
        print("I gave you {:d}".format(self.cash))
        self.cash = 0
    
    def remaining_action(self):
        print("The coffee machine has:")
        print("{:d} of water".format(self.water))
        print("{:d} of milk".format(self.milk))
        print("{:d} of coffee beans".format(self.coffee_beans))
        print("{:d} of disposable cups".format(self.disposable_cups))
        print("{:d} of money".format(self.cash))
        print("")

coffee_machine_1 = CoffeeMachine()

while coffee_machine_1.status != "exit":
    coffee_machine_1.status = input("Write action (buy, fill, take, remaining, exit): ")
    if coffee_machine_1.status == "buy":
        coffee_machine_1.choose_buy_action()
    elif coffee_machine_1.status == "fill":
        coffee_machine_1.fill_action()
    elif coffee_machine_1.status == "take":
        coffee_machine_1.take_action()
    elif coffee_machine_1.status == "remaining":
        coffee_machine_1.remaining_action()