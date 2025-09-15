# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def report():
    """Prints a report of current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def is_resource_sufficient(drink):
    """Checks if there are enough resources to make the drink."""
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is accepted, or False if not."""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
    resources["money"] += drink_cost
    return True


def make_coffee(drink):
    """Deducts resources and serves coffee."""
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            report()
        elif choice in MENU:
            if is_resource_sufficient(choice):
                payment = process_coins()
                if is_transaction_successful(payment, MENU[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid option. Please choose espresso, latte, or cappuccino.")


coffee_machine()
