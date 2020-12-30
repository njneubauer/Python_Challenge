import os 
import csv
import sys

# Input & Output files
budget_data = os.path.join("Resources", "budget_data.csv")
analysis_output = os.path.join("Analysis", "Analysis_Results.txt")

# Print line used in results to create sections
lineBreak = "----------------------------"

# PyBank Analysis

with open(budget_data, 'r') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    
    # Month Variables
    numMonths = 0

    # Gain/Loss Netprofit
    gains_losses = []
    netProfit = 0

    # Average Change Variables
    currMonthVal = None
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
            maxIncrease = avgChgVal
            minDecrease = avgChgVal
        # Grab Max Increase month & value
        if avgChgVal > maxIncrease:
            maxProfMonth = str(row[0])
            maxIncrease = avgChgVal
        # Grab Min Decrease month & value
        if avgChgVal < minDecrease:
            minProfMonth = str(row[0])
            minDecrease = avgChgVal 

    # Calculates average change 1 time outside "for loop"
    averageChange = round(sum(avgChgList) / len(avgChgList),2)
 
# Function to print results with less lines of code. 
def pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease):
    print(" ")
    print("Financial Analysis")
    print(lineBreak)
    print(f"     Total Months: {numMonths}")
    print(f"       Net Profit: $ {currFormat(netProfit)}")
    print(f"   Average Change: $ {currFormat(averageChange)}")
    print(f"Greatest Increase: {maxProfMonth} (${currFormat(maxIncrease)})")
    print(f"Greatest Decrease: {minProfMonth} (${currFormat(minDecrease)})\n")

# Print to Terminal
pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease)

# Print results to text file. Website where learned about sys.stdoubt = https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
with open(analysis_output, 'w') as results:
    orig_stdout = sys.stdout
    sys.stdout = results
    pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease)
    sys.stdout = orig_stdout
