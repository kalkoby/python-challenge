print ("You fetch main.py of PyBank")

#Date,Profit/Losses

import os
import csv


bank_budget_csv = os.path.join(".", "Resources", "budget_data.csv")

months = 0 
total = 0
change = 0
prevPrice = 0.00
changePrice = 0.00
avgChange = 0.00


with open(bank_budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    
     # Read through each row of data after the header
    for row in csvreader: 
        #Count months
        months += 1

        total += float(row[1])
        if months == 1 :
            prevPrice = float(row[1])

        if months > 1:
            changeTotal = float(row[1]) - prevPrice 
            changePrice = changePrice + changeTotal
            prevPrice = float(row[1])

avgChange = changePrice / (months - 1)
print ("Financial Analysis")
print ("")
print ("------------------------------------")
print(f"Total Months: {months}")
print(f"Total: {total}")
print(f"Average Change: {avgChange}")

    
    

