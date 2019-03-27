import os
import csv


def printNwrite(msg):
    print(msg)
    writer.write(msg + "\n") 

# Set variable and open the output file
output_file = os.path.join("./Resources","voteSummary.txt")
writer = open(output_file,"w",newline="")

votes=0
candidates = []
nbrVotes = []
percVotes=0
count = 0


election_data_csv = os.path.join(".", "Resources", "election_data.csv")

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # and not to print(f"Header: {csv_header}") 

    
     # Read through each row of data after the header
    for row in csvreader:      
        #Count vote
        votes += 1
        Found = False

        # check if a candidate is already in the list, if not add to the list
        for name in candidates:
            if name == row[2] :
                Found = True
                #candyList.index(candy))
                # pie_purchases[choice_index] += 1
                
                selected = candidates.index(row[2])     
                nbrVotes[selected] += 1        
                break 
        
        if Found == False:
            candidates.append(row[2])
            nbrVotes.append(1)


printNwrite("Election Results")
printNwrite("_____________________")
printNwrite("")

printNwrite(f"Total Votes: {votes}")
printNwrite("_____________________")
printNwrite("")
count = 0
maxVote = 0

for printName in candidates:
    percVote = round((nbrVotes[count] / votes) * 100,3)      
    printNwrite(f"{printName}: {percVote}% ({nbrVotes[count]}) ")
    
    if nbrVotes[count] > maxVote:
        maxVote = nbrVotes[count] 
        winner = candidates[count]
    
    count += 1
printNwrite("_____________________")
printNwrite("")
printNwrite(f"Winner : {winner}")
printNwrite("")
printNwrite("_____________________")