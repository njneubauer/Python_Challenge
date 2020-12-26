import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
lineBreak = "----------------------------"

with open(election_data) as electionFile:
    csvreader = csv.reader(electionFile, delimiter=',')
    # Skip header row
    csv_header = next(csvreader)

    # Variables total votes
    vote_total = 0
    num_format = '{:,}'.format

    # candidate variables
    candidate = " "
    correy_list = []
    khan_list = []
    li_list = []
    otooley_list = []
    votes_rec = 0
    def vote_percent(data):  
        x = round((len(data)/vote_total)*100,2)
        return(f"{x} %")
    for row in csvreader:
        vote_total += 1
        candidate = row[2]
        candidate = candidate.lower()
        if candidate == "khan":
            khan_list.append(candidate.lower())
        elif candidate == "correy":
            correy_list.append(candidate.lower())
        elif candidate == "li":
            li_list.append(candidate.lower())
        elif candidate == "o'tooley":
            otooley_list.append(candidate.lower())
        else:
            print(f"ERROR: datapoint in row {vote_total} doesn't match any candidate. Fix and rerun data")
            break
        
print("Election Results")
print(lineBreak)
print(f"Total Votes:  {num_format(vote_total)}")
print(lineBreak)
print(f"       Kahn:  {vote_percent(khan_list)} ({len(khan_list)})")
print(f"     Correy:  {vote_percent(correy_list)} ({len(correy_list)})")
print(f"         Li:  {vote_percent(li_list)} ({len(li_list)})")
print(f"   O\'Tooley:   {vote_percent(otooley_list)} ({len(otooley_list)})")
print(lineBreak)
print(f"Winner: {}")