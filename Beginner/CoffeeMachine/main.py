import calculations

ON = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money_stored = 0.0


def coffee_machine():
    global ON
    global money_stored
    global resources
    global MENU

    want = input("What would you like? (espresso/latte/cappuccino): ")

    if want == "report":
        calculations.report(resources, money_stored)
    elif want == "off":
        ON = False

    else:
        possible = calculations.check_availability(resources, MENU, want)
        if possible:
            resources, money_stored = calculations.money_calculations(money_stored, resources, MENU, want)





while ON:
    coffee_machine()
