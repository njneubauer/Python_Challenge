import os
import csv
import sys

# Input & Output files
election_data = os.path.join("Resources", "election_data.csv")
analysis_output = os.path.join("Analysis", "Analysis_Results.txt")

# Print line used in results to create sections
lineBreak = "------------------------------"

# Pypoll Analysis

# Open .csv file for processing
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

# Process Votes--lowercase input to avoid data entry errors related to capitalization
    for row in csvreader:
        # Count total votes
        vote_total += 1
        # Prepare data by lowercasing all inputs for vote processing
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
            # Stop program if datapoint exists that doesn't match processing conditions. Print line# where error occured.
            print(f"ERROR: datapoint in row {vote_total} doesn't match any candidate. Fix data and rerun script")
            exit()

    # Determine winner or if a tie exists
    if khan_votes > correy_votes and li_votes and otooley_votes:
        winner = "Khan"
    elif correy_votes and li_votes and otooley_votes and khan_votes:
        winner = "Correy"
    elif li_votes > correy_votes and khan_votes and otooley_votes:
        winner = "Li"
    elif otooley_votes > correy_votes and khan_votes and li_votes:
        winner = "Li"
    else: 
        winner = "tie"

# Function to print results with less lines of code
def pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner):
    print(" ")
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
pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner)

# Print results to text file. Website where learned about sys.stdoubt = https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
with open(analysis_output, 'w') as results:
    orig_stdout = sys.stdout
    sys.stdout = results
    pypoll_results(lineBreak,vote_total,khan_votes,correy_votes,li_votes,otooley_votes, winner)
    sys.stdout = orig_stdout