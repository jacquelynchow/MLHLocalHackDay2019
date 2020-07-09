import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def readFile():
    datesFile = open("dataDates.txt", 'r')
    spendingFile = open("dataMoneySpent.txt", 'r')

    datesList = []
    for date in datesFile:
        start = len(date) - 1
        stop = len(date)
        date = date[0: + start:] + date[stop: + 1:]
        datesList.append(date)
    datesFile.close()

    spendingList = []
    for spent in spendingFile:
        start = len(spent) - 1
        stop = len(spent)
        spent = spent[0: + start:] + spent[stop: + 1:]
        spendingList.append(spent)
    spendingFile.close()

    myDatesList = []
    mySpendList = []
    sameDays = 1
    for j in range(len(datesList)):
        if j != len(datesList) - 1:
            if datesList[j] == datesList[j+1]:
                sameDays+=1

    for i in range(len(datesList) - sameDays):
        # add first date to the list
        myDatesList.append(datesList[i])
        # check by looping if there are other dates that are the same
        while datesList[i] == datesList[i+1]:
            spent = float(spendingList[i]) + float(spendingList[i+1])
            mySpendList.append(spent)
            i+=1
        myDatesList.append(datesList[i])
        mySpendList.append(spendingList[i])

    # make the new file with the costs (the index represents number of days)
    outfile = open("spendingDataForGraph.txt", "w+")
    for k in range(len(mySpendList)):
        outfile.write(str(mySpendList[k]) + "\n")
    outfile.close()

    # days, spending = np.loadtxt("daysandspending.txt", unpack=True,
    #     converters={ 0: mdates.strpdate2num("%Y-%m-%d")})
    # plt.plot_date(x=days, y=spending)
    # plt.show()

def main():
    readFile();
main()
