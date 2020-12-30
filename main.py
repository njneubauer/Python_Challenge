import os 
import csv
import sys

# PyBank Analysis
budget_data = os.path.join("Resources", "budget_data.csv")
analysis_output = os.path.join("Analysis", "Analysis_Results.txt")

lineBreak = "------------------------------"

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
 
# function to print results to screen & to text file
def pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease):
    print(" ")
    print("Financial Analysis")
    print(lineBreak)
    print(f"     Total Months: {numMonths}")
    print(f"       Net Profit: $ {currFormat(netProfit)}")
    print(f"   Average Change: $ {currFormat(averageChange)}")
    print(f"Greatest Increase: {maxProfMonth} (${currFormat(maxIncrease)})")
    print(f"Greatest Decrease: {minProfMonth} (${currFormat(minDecrease)})\n")

# Pypoll Analysis
election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as electionFile:
    csvreader = csv.reader(electionFile, delimiter=',')
    # Skip header row
    csv_header = next(csvreader)

    # Variables total votes
    vote_total = 0
    num_format = '{:,}'.format

    # candidate variables
    candidate = " "
    correy_votes = 0
    khan_votes = 0
    li_votes = 0
    otooley_votes = 0
    winner = " "

    # function to do calculations
    def vote_calc(vote_data):  
        percent = round((vote_data/vote_total)*100,2)
        candidate_total = vote_data
        return(f"{percent} % ({candidate_total})")

    # Process Votes 
    for row in csvreader:
        vote_total += 1
        candidate = row[2]
        candidate = candidate.lower()
        if candidate == "khan":
            khan_votes += 1
            
        elif candidate == "correy":
            correy_votes += 1
        elif candidate == "li":
            li_votes += 1
        elif candidate == "o'tooley":
            otooley_votes += 1
        else:
            print(f"ERROR: datapoint in row {vote_total} doesn't match any candidate. Fix data and rerun script")
            exit()

    if khan_votes > correy_votes and li_votes and otooley_votes:
        winner = "Khan"
    elif correy_votes and li_votes and otooley_votes and khan_votes:
        winner = "Correy"
    elif li_votes > correy_votes and khan_votes and otooley_votes:
        winner = "Li"
    elif otooley_votes > correy_votes and khan_votes and li_votes:
        winner = "Li"
    else: 
        winner = "tie, need a tiebreaker"

# function to print results to screen & to text file
def pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner):
    print("Election Results")
    print(lineBreak)
    print(f"Total Votes:  {num_format(vote_total)}")
    print(lineBreak)
    print(f"       Kahn:  {vote_calc(khan_votes)}")
    print(f"     Correy:  {vote_calc(correy_votes)}")
    print(f"         Li:  {vote_calc(li_votes)}")
    print(f"   O\'Tooley:   {vote_calc(otooley_votes)}")
    print(lineBreak)
    print(f"Winner: {winner}")
    print(lineBreak)

# Print results to terminal screen
pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease)
pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner)

# Print results to text file. Website where learned about sys.stdoubt = https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
with open(analysis_output, 'w') as results:
    orig_stdout = sys.stdout
    sys.stdout = results
    pybank_results(lineBreak,numMonths,netProfit,averageChange,maxProfMonth,maxIncrease,minProfMonth,minDecrease)
    pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner)
    sys.stdout = orig_stdout