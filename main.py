import os 
import csv

budget_dataCsv = os.path.join("Resources", "budget_data.csv")

lineBreak = "----------------------------"

# PyBank
with open(budget_dataCsv, 'r') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    
    # Month Variables
    numMonths = 0

    # Gain/Loss Netprofit
    gains_losses = []
    netProfit = 0

    # Average Change Variables
    currMonthVal = 0
    prevMonthVal = None
    avgChgVal = 0
    avgChgList = []
    averageChange = 0

    # Greatest Increase/Greatest Decrease variables
    MaxIncrease = None
    MinDecrease = None
    MaxProfMonth = " "
    MinProfMonth = " "
    
    # format currency data
    currFormat = '{:,}'.format

    # Skip the header in .csv file
    csv_header = next(csvreader)

    # CSV reader loop through data
    for row in csvreader:
        # Add months
        numMonths += 1
        # Sum gains/losses
        gains_losses.append(int(row[1]))
        netProfit = sum(gains_losses)
        # Average Change & Greatest Increase/Decrease loop
        if prevMonthVal:
            prevMonthVal = int(currMonthVal)
            currMonthVal = int(row[1])
            avgChgVal = (prevMonthVal - currMonthVal)*-1
            avgChgList.append(avgChgVal)
        else:
            currMonthVal = int(row[1])
            prevMonthVal = currMonthVal
            MaxIncrease = avgChgVal
            MinDecrease = avgChgVal
        # Grab Max Increase month & value
        if avgChgVal > MaxIncrease:
            MaxProfMonth = str(row[0])
            MaxIncrease = avgChgVal
        # Grab Min Decrease month & value
        if avgChgVal < MinDecrease:
            MinProfMonth = str(row[0])
            MinDecrease = avgChgVal 

    # Calculates average change 1 time outside "for loop"
    averageChange = round(sum(avgChgList) / len(avgChgList),2)
 
    # Print Results
    print(" ")
    print("Financial Analysis")
    print(lineBreak)
    print(f"Total Months:  {numMonths}")
    print(f"Net Profit:     $ {currFormat(netProfit)}")
    print(f"Average Change: $ {currFormat(averageChange)}")
    print(f"Greatest Increase: {MaxProfMonth} (${currFormat(MaxIncrease)})")
    print(f"Greatest Decrease: {MinProfMonth} (${currFormat(MinDecrease)})")