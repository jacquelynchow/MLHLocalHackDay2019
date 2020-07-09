from category import *
from datetime import *

class Tracker:
    def __init__(self, budget = 0, balance = 0):
        self.budget = budget
        self.balance = balance
        self.categories = dict()

    def getBudget(self):
        return self.budget

    def set_budget(self):
        if self.budget > 0:
            check = input("You already set a budget for this month, are you sure you want to change it? [Y/N] ")
            while(check != "Y" and check != "N"):
                check = input("Please enter 'Y' or 'N' to indicate whether or not you want to reset your budget: ")
            if check == "N":
                return

        budget = input("What would you like your monthly budget to be? ")
        while budget.isdigit() == False or int(budget) <= 0:
            budget = input("Please enter a valid budget: ")
        self.budget = int(budget)

    def add_category(self):
        name = input("What category would you like to add? ")
        while name in self.categories:
            name = input("It seems you already have this category. Type 'quit' or try a different name: ")
            if name == "quit":
                return
        new_category = Category(name)
        self.categories[new_category.getName()] = new_category
        return new_category

    def add_purchase(self):
        amt = input("Please enter the amount spent: $")
        while amt.isdigit() == False or int(amt) < 0:
            amt = input("Please enter a positive, valid amount: ")
        c = input("What category would this purchase fit under? ")

        try:
            self.categories[c].addAmount(int(amt))
        except KeyError:
            print("You have not made this category yet, please add a new one: ")
            c = self.add_category()
            self.categories[c].addAmount(int(amt))

        self.balance += int(amt)

    def print_tracker(self):
        current_date = date.today()
        print("The current date is", current_date.strftime("%b %d %Y"))
        for c in self.categories:
            print(self.categories[c])
        print("Your current balance for the month is: $%.2f" % (self.balance))
        print("Your monthly budget is: $%.2f" % (self.budget))

        # Is there a way to keep track of the days until the end of the same month?
