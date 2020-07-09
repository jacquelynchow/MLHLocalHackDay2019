

# importing the required module
import matplotlib.pyplot as plt
from matplotlib.dates import (DAILY, DateFormatter, rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime

print "\n Welcome to the Swarthmore Meal Plan Visual Budget Tool"
print "========================================================="
mealPlan = raw_input("Enter your meal plan: ")

if mealPlan == "SWAT":
    # print "SWAT"
    diningDols = 150/55
elif mealPlan == "GARNET":
    # print "GARNET"
    diningDols = 300/55
elif mealPlan == "PHOENIX":
    # print "PHOENIX"
    diningDols = 400/55
elif mealPlan == "PARRISH":
    # print "PARRISH"
    diningDols = 500/55
elif mealPlan == "PPR":
    # print "PPR"
    diningDols = 200/55
elif mealPlan == "COMMUTER":
    # print "COMMUTER"
    diningDols = 100/55
else:
    print "Not a valid meal plan."

graphType = 0
# while graphType != 3:
graphType = raw_input("Please enter choose a graph type, 1 or 2: ")
y = []
y2 = []
if int(graphType) == 1:
    sum = 0.0
    spendingFile = open("spendingDataForGraph.txt", 'r')
    for amt in spendingFile:
        # print amt.strip()
        y.append(float(amt.strip()))
        sum += float(amt.strip())
    avg = sum/55

    for i in range(55):
        y2.append(diningDols)
else:
    sum = 0.0
    spendingFile = open("spendingDataForGraph.txt", 'r')
    for amt in spendingFile:
        y.append(sum)
        sum += float(amt.strip())
    avg = sum/55

    for i in range(55):
        y2.append(diningDols*(i+1))


# y3 = []
# for i in range(55):
#     y3.append(avg)


# if graphType != 3:
    #8/27 - 12/3
np.random.seed(19680801)
# tick every 5th easter
# rule = rrulewrapper(DAILY, interval=70)
# loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
date1 = datetime.date(2019, 8, 27)
date2 = datetime.date(2019, 12, 03)
date3 = datetime.date(2019, 8, 27)
x = []
for i in range(1, len(y)+1):
    x.append(i)

# x.append(date2)
# date3 = datetime.date(2000, 1, 30)
delta = datetime.timedelta(days=100)
# x axis values
# corresponding y axis values
# fig, ax = plt.subplots()
# plotting the points
plt.plot(x, y, label = "Current Spending")
plt.plot(x, y2, label = "Budgeted Spending")
# plt.plot(x, y3, label = "Projected Spending")

# ax.xaxis.set_major_locator(loc)
# ax.xaxis.set_major_formatter(formatter)
# ax.xaxis.set_tick_params(rotation=30, labelsize=10)

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Amount Spent ($)')

plt.legend()

# giving a title to my graph
plt.title('Meal Plan Budgeting: ' + mealPlan)
# print x
# print y

# function to show the plot
plt.show()
