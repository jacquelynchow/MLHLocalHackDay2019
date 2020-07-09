class Category:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBalance(self):
        return self.balance

    def addAmount(self, amt):
        self.balance += amt
        print("Updated *%s* balance: $%.2f" % (self.name, self.balance))

    def __str__(self): 
        return "Balance for *%s*: $%.2f" % (self.name, self.balance)
