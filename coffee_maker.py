def state_coffee_machine_start():
    water = 400
    milk = 540 
    coffee_beans = 120
    disposable_cups = 9
    cash = 550
    list_start = [water, milk, coffee_beans, disposable_cups, cash]
    print("The coffee machine has:")
    print("{:d} of water".format(water))
    print("{:d} of milk".format(milk))
    print("{:d} of coffee beans".format(coffee_beans))
    print("{:d} of disposable cups".format(disposable_cups))
    print("{:d} of money".format(cash))
    print("")
    return list_start

def choose_action(list_):
    action = input("Write action (buy, fill, take): ")
    print("")
    if action == "buy":
        return choose_buy_action(list_[0], list_[1], list_[2], list_[3], list_[4])
    elif action == "fill":
        return fill_action(list_[0], list_[1], list_[2], list_[3], list_[4])
    elif action == "take":
        return take_action(list_[0], list_[1], list_[2], list_[3], list_[4])

    
def choose_buy_action(water, milk, coffee_beans , disposable_cups, cash):
    kind_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    print("")
    if kind_of_coffee == "1":
        return buy_action_espresso(water, milk, coffee_beans , disposable_cups, cash)
    elif kind_of_coffee == "2":
        return buy_action_latte(water, milk, coffee_beans , disposable_cups, cash)
    elif kind_of_coffee == "3":
        return buy_action_cappuccino(water, milk, coffee_beans , disposable_cups, cash)

def buy_action_espresso(water, milk, coffee_beans , disposable_cups, cash):
    water -= 250
    milk = milk
    coffee_beans -= 16
    disposable_cups -= 1
    cash += 4
    return state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash) 

def buy_action_cappuccino(water, milk, coffee_beans , disposable_cups, cash):
    water -= 200
    milk -= 100
    coffee_beans -= 12
    disposable_cups -= 1
    cash += 6
    return state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash)

def buy_action_latte(water, milk, coffee_beans, disposable_cups, cash):
    water -= 350
    milk -= 75
    coffee_beans -= 20
    disposable_cups -= 1
    cash += 7
    return state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash)

def fill_action(water, milk, coffee_beans, disposable_cups, cash):
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += add_water
    milk += add_milk
    coffee_beans += add_coffee_beans
    disposable_cups += add_disposable_cups
    return state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash)

def take_action(water, milk, coffee_beans, disposable_cups, cash):
    money_paid_out = cash
    cash -= money_paid_out
    return state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash)

def state_coffee_machine_end(water, milk, coffee_beans, disposable_cups, cash):
    print("The coffee machine has:")
    print("{:d} of water".format(water))
    print("{:d} of milk".format(milk))
    print("{:d} of coffee beans".format(coffee_beans))
    print("{:d} of disposable cups".format(disposable_cups))
    print("{:d} of money".format(cash))



choose_action(state_coffee_machine_start())




