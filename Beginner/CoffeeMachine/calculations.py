def report(resources, money_stored):
    for key in resources:
        print(str(key) + ":", (resources[key]), "ml")
    print("Money: $" + str(money_stored))

def check_availability(resources, MENU, want):
    ingredients = ["water", "milk", "coffee"]
    if all(resources[item] >= MENU[want]['ingredients'][item] for item in ingredients):
        return True
    else:
        for item in ingredients:
            if resources[item] < MENU[want]['ingredients'][item]:
                print("Sorry there is not enough", item)
        return False

def money_calculations(money_stored, resources, MENU, want):
    print('Please insert coins.')
    quarters = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickels = float(input("How many nickels?:"))
    pennies = float(input("How many pennies?:"))
    total_paid = ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))


    change = total_paid - MENU[want]['cost']
    if change > 0:
        print("Here is your $", change, "in change")
        print("Here is your", want)
        print("Enjoy!")
        money_stored = money_stored + MENU[want]["cost"]

        for item in resources:
            resources[item] = resources[item] - MENU[want]["ingredients"][item]






    elif change < 0:
        print("Sorry not enough money, thus we are refunding your money")

    return resources, money_stored


