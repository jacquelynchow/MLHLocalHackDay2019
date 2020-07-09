from tracker import *

def print_options():
    print("Please select one of the following:")
    print("1. Set budget")
    print("2. See tracker")
    print("3. Add category")
    print("4. Add purchase")
    print("5. Quit")

def get_choice():
    print("If you would like to see the options again, enter 0.")
    selection = input("Option [0, 1, 2, 3, 4, 5]? ")
    while selection.isdigit() == False or int(selection) > 5 or int(selection) < 0:
        selection = input("Please select option 0, 1, 2, 3, 4, or 5. Option? ")
    return int(selection)

# def main():
#     print("\nWelcome to your personal spending tracker!")
#     print("~" * 42)
#     print_options()
#     print("-" * 50)
#
#     t = Tracker()
#     while True:
#         choice = get_choice()
#         if choice == 0:
#             print_options()
#         elif choice == 1:
#             t.set_budget()
#         elif choice == 2:
#             t.print_tracker()
#         elif choice == 3:
#             t.add_category()
#         elif choice == 4:
#             if t.getBudget() == 0:
#                 t.set_budget()
#             t.add_purchase()
#         else:
#             quit()
#         print("-" * 50)
# main()
