from prettytable import PrettyTable

class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        table = PrettyTable()
        table.field_names = ["Resource", "Amount"]
        table.add_row(["Water", f"{self.resources['water']}ml"])
        table.add_row(["Milk", f"{self.resources['milk']}ml"])
        table.add_row(["Coffee", f"{self.resources['coffee']}g"])
        print(table)

    def is_resource_sufficient(self, drink):
        for item, amount in drink.ingredients.items():
            if self.resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        for item, amount in drink.ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {drink.name}. Enjoy!")
