import sys

def state_coffee_machine_start():
    water = 400
    milk = 540 
    coffee_beans = 120
    disposable_cups = 9
    cash = 550
    list_start = [water, milk, coffee_beans, disposable_cups, cash]
    return list_start

def choose_action(list_):
    action = input("Write action (buy, fill, take, remaining, exit): ")
    print("")
    if action != "exit":
        if action == "buy":
            return choose_buy_action(list_[0], list_[1], list_[2], list_[3], list_[4])
        elif action == "fill":
            return fill_action(list_[0], list_[1], list_[2], list_[3], list_[4])
        elif action == "take":
            return take_action(list_[0], list_[1], list_[2], list_[3], list_[4])
        elif action == "remaining":
            return remaining_action(list_[0], list_[1], list_[2], list_[3], list_[4])
    if action == "exit":
        sys.exit()

def choose_buy_action(water, milk, coffee_beans , disposable_cups, cash):
    kind_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu: ")
    print("")
    if kind_of_coffee == "1":
        return buy_action_espresso(water, milk, coffee_beans , disposable_cups, cash)
    elif kind_of_coffee == "2":
        return buy_action_latte(water, milk, coffee_beans , disposable_cups, cash)
    elif kind_of_coffee == "3":
        return buy_action_cappuccino(water, milk, coffee_beans , disposable_cups, cash)
    elif kind_of_coffee == "back":
        list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
        return choose_action(list_after_transaction)

def buy_action_espresso(water, milk, coffee_beans , disposable_cups, cash):
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    if (water >= 250 and milk >= 0 and coffee_beans >= 16 and disposable_cups >= 1):
        water -= 250
        milk = milk
        coffee_beans -= 16
        disposable_cups -= 1
        cash += 4
        list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
        print("I have enough resources, making you a coffee!")
        print("")
        return choose_action(list_after_transaction)
    else:
        if water < 250:
            print("Sorry, not enough water!")
        if coffee_beans < 16:
            print("Sorry, not enough coffe beans!")
        if disposable_cups < 1:
            print("Sorry, not enough disposable cups!")   
        return(choose_action(list_after_transaction))

def buy_action_cappuccino(water, milk, coffee_beans , disposable_cups, cash):
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    if (water >= 200 and milk >= 100 and coffee_beans >= 12 and disposable_cups >= 1):
        water -= 200
        milk -= 100
        coffee_beans -= 12
        disposable_cups -= 1
        cash += 6
        list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
        print("I have enough resources, making you a coffee!")
        print("")
        return choose_action(list_after_transaction)
    else:
        if water < 200:
            print("Sorry, not enough water!")
        if milk < 100:
            print("Sorry, not enough milk!")
        if coffee_beans < 12:
            print("Sorry, not enough coffe beans!")
        if disposable_cups < 1:
            print("Sorry, not enough disposable cups!")   
        return(choose_action(list_after_transaction))

def buy_action_latte(water, milk, coffee_beans, disposable_cups, cash):
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    if (water >= 350 and milk >= 75 and coffee_beans >= 20 and disposable_cups >= 1):
        water -= 350
        milk -= 75
        coffee_beans -= 20
        disposable_cups -= 1
        cash += 7
        list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
        print("I have enough resources, making you a coffee!")
        print("")
        return choose_action(list_after_transaction)
    else:
        if water < 350:
            print("Sorry, not enough water!")
        if milk < 75:
            print("Sorry, not enough milk!")
        if coffee_beans < 20:
            print("Sorry, not enough coffe beans!")
        if disposable_cups < 1:
            print("Sorry, not enough disposable cups!")   
        return(choose_action(list_after_transaction))

def fill_action(water, milk, coffee_beans, disposable_cups, cash):
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += add_water
    milk += add_milk
    coffee_beans += add_coffee_beans
    disposable_cups += add_disposable_cups
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    return choose_action(list_after_transaction)

def take_action(water, milk, coffee_beans, disposable_cups, cash):
    money_paid_out = cash
    print("I gave you {:d}".format(cash))
    cash -= money_paid_out
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    return choose_action(list_after_transaction)

def remaining_action(water, milk, coffee_beans, disposable_cups, cash):
    print("The coffee machine has:")
    print("{:d} of water".format(water))
    print("{:d} of milk".format(milk))
    print("{:d} of coffee beans".format(coffee_beans))
    print("{:d} of disposable cups".format(disposable_cups))
    print("{:d} of money".format(cash))
    print("")
    list_after_transaction = [water, milk, coffee_beans, disposable_cups, cash]
    return choose_action(list_after_transaction)

choose_action(state_coffee_machine_start())