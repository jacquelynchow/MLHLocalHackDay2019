from user import *

class Budget:
    def __init__(self, swipes, dollars, points):

        self.cur_swipes = swipes
        self.cur_dollars = dollars
        self.cur_points = points

        # budget
        self.daily_swipes = 0
        self.daily_dollars = 0
        self.daily_points = 0

        self.weekly_swipes = 0
        self.weekly_dollars = 0
        self.weekly_points = 0

        self.days_left = 0
        self.weeks_left = 0

def mealplan():
    """
    Asks user to select meal plan
    Returns meal plan
    """
    print("Select your meal plan:")
    print("      (a) Swat")
    print("      (b) Garnet")
    print("      (c) Phoenix")
    print("      (d) Parrish")
    print("      (e) PPR Apts")
    print("      (f) Commuter")

    plan = input("")
    lst = []
    if plan == "a":
        lst.append(999) # swipes
        lst.append(150) # dining dollars
        lst.append(150) # swat points
    elif plan == "b":
        lst.append(275) # swipes
        lst.append(300) # dining dollars
        lst.append(200) # swat points
    elif plan == "c":
        lst.append(225) # swipes
        lst.append(400) # dining dollars
        lst.append(300) # swat points
    elif plan == "d":
        lst.append(160) # swipes
        lst.append(500) # dining dollars
        lst.append(400) # swat points
    elif plan == "e":
        lst.append(160) # swipes
        lst.append(200) # dining dollars
        lst.append(700) # swat points
    elif plan == "f":
        lst.append(100) # swipes
        lst.append(100) # dining dollars
        lst.append(0) # swat points
    else:
        print("Please enter a,b,c,d,e, or f")

    return lst

def print_budget(budget):
    """
    prints current status on all 3 accounts and week/day budget
    """

    budget.daily_swipes = budget.cur_swipes / budget.days_left
    budget.weekly_swipes = budget.cur_swipes / budget.weeks_left

    budget.daily_dollars = budget.cur_dollars / budget.days_left
    budget.weekly_dollars = budget.cur_dollars / budget.weeks_left

    budget.daily_points = budget.cur_points / budget.days_left
    budget.weekly_points = budget.cur_points / budget.weeks_left

    print()
    print("======= Your Current Status for this Semester =======")
    print("%d swipes left" %(budget.cur_swipes))
    print("%.2f dining dollars left" %(budget.cur_dollars))
    print("%.2f Swat points left" %(budget.cur_points))

    print()
    print("======= Budget =======")
    print("%.2f swipes / week, %.2f / day" %(budget.weekly_swipes, budget.daily_swipes))
    print("%.2f dollars / week, %.2f / day" %(budget.weekly_dollars, budget.daily_dollars))
    print("%.2f points / week, %.2f / day" %(budget.weekly_points, budget.daily_points))
    print()

def process(budget):
    """
    processes a transaction and recalculates Budget
    """
    print("A transaction occurred!")
    print()

    # read in transaction file
    # format: date, time, account, amount spent
    print("Reading in a transaction file...")
    print()
    filename = "/home/schang1/MLHLocalHackDay2019/transaction.txt"
    file = open(filename, 'r')
    file_list = []

    for line in file:
        line = line.strip()
        file_list.append(line)

    account = file_list[2]
    expense = file_list[3]

    if account == "Meal":
        budget.cur_swipes = budget.cur_swipes - int(expense)
        budget.daily_swipes = budget.cur_swipes / budget.days_left
        budget.weekly_swipes = budget.cur_swipes / budget.weeks_left
    elif account == "Dining Dollars":
        budget.cur_dollars = budget.cur_dollars - float(expense)
        budget.daily_dollars = budget.cur_dollars / budget.days_left
        budget.weekly_dollars = budget.cur_dollars / budget.weeks_left
    elif account == "Swat Points":
        budget.cur_points = budget.cur_points - float(expense)
        budget.daily_points = budget.cur_points / budget.days_left
        budget.weekly_points = budget.cur_points / budget.weeks_left


    file.close()
    print("Transcation of using %s %s processed." %(expense,account))
    print()

def personal():
    print("\nWelcome to your personal spending tracker!")
    print("~" * 42)
    print_options()
    print("-" * 50)

    t = Tracker()
    while True:
        choice = get_choice()
        if choice == 0:
            print_options()
        elif choice == 1:
            t.set_budget()
        elif choice == 2:
            t.print_tracker()
        elif choice == 3:
            t.add_category()
        elif choice == 4:
            if t.getBudget() == 0:
                t.set_budget()
            t.add_purchase()
        else:
            quit()
        print("-" * 50)

def main():

    plan = mealplan()

    # initialize budget
    budget = Budget(int(plan[0]), float(plan[1]), float(plan[2]))


    # budget.cur_swipes = plan[0]
    # budget.cur_dollars = plan[1]
    # budget.cur_points = plan[2]
    print()
    print("For this semester, you have:")
    print("      %d meal swipes" %budget.cur_swipes)
    print("      %d dining dollars" %budget.cur_dollars)
    print("      %d Swat points" %budget.cur_points)
    print()
    print("Let's set up a budget.")
    print()


    # calculate how many days on campus
    fallbreak = int(input("For how many days of Fall Break will you be on campus (0-9)? "))
    while fallbreak not in range(10):
        print("Invalid input. Enter a value 0-9.")
        print()
        fallbreak = int(input("For how many days of Fall Break will you be on campus (0-9)? "))

    thanksgiving = int(input("For how many days of Thanksgiving break will you be on campus (0-4)? "))
    print()
    budget.days_left = 99 + fallbreak + thanksgiving
    budget.weeks_left = budget.days_left / 7



    # recommended Budget
    budget.daily_swipes = budget.cur_swipes / budget.days_left
    budget.weekly_swipes = budget.cur_swipes / budget.weeks_left

    budget.daily_dollars = budget.cur_dollars / budget.days_left
    budget.weekly_dollars = budget.cur_dollars / budget.weeks_left

    budget.daily_points = budget.cur_points / budget.days_left
    budget.weekly_points = budget.cur_points / budget.weeks_left

    print("Based on your meal plan, we recommend using:")
    print("      %.2f swipes / week, %.2f / day" %(budget.weekly_swipes, budget.daily_swipes))
    print("      %.2f dollars / week, %.2f / day" %(budget.weekly_dollars, budget.daily_dollars))
    print("      %.2f points / week, %.2f / day" %(budget.weekly_points, budget.daily_points))
    print()

    while True:
        view = input("Type 'b' to view current weekly/daily budget and current status.\nType 't' to process a OneCard transaction.\nType 'p' to track your personal spending.\nType 'q' to quit. ")
        print()
        if view == "b":
            print_budget(budget)
        elif view == "t":
            process(budget)
        elif view == "p":
            personal()
        elif view == "q":
            quit()
        else:
            print("Invalid input.")

main()
