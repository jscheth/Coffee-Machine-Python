from prettytable import PrettyTable

class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        table = PrettyTable()
        table.field_names = ["Report", "Value"]
        table.add_row(["Money Collected", f"{self.CURRENCY}{self.profit:.2f}"])
        print(table)

    def process_coins(self):
        print("Please insert coins.")
        self.money_received = 0
        for coin, value in self.COIN_VALUES.items():
            count = int(input(f"How many {coin}?: "))
            self.money_received += count * value
        return round(self.money_received, 2)

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(self.money_received - cost, 2)
        if change > 0:
            print(f"Here is {self.CURRENCY}{change} in change.")
        self.profit += cost
        return True
