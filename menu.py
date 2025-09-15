class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.items = [
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("cappuccino", 250, 100, 24, 3.0),
        ]

    def get_items(self):
        return "/".join(item.name for item in self.items)

    def find_drink(self, order_name):
        for item in self.items:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")
        return None