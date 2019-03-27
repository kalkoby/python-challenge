import os
import csv

votes=0

print ("It is inside of the PYROLL for main.py")
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # and not to print(f"Header: {csv_header}") 

    
     # Read through each row of data after the header
    for row in csvreader:      
        #Count months
        votes += 1

print(f"Total Votes: {votes}")