#print ("You fetch main.py of PyBank") 
#Date,Profit/Losses

import os
import csv

def printNwrite(msg):
    print(msg)
    writer.write(msg + "\n") 

def createSummary():
    avgChange = changePrice / (months - 1)
    printNwrite("Financial Analysis")
    printNwrite("------------------------------------")
    printNwrite(f"Total Months: {months}")
    printNwrite(f"Total: {total}")
    printNwrite(f"Average Change: {avgChange}")
    printNwrite(f"Greatest Increase in Profits: {gProfitDate} (${greatProfit})")
    printNwrite(f"Greatest Decrease in Profits: {lProfitDate} (${greatLoss})")


months = 0 
total = 0
change = 0
changeTotal = 0
greatLoss = 0.00
greatProfit = 0.00
prevPrice = 0.00
changePrice = 0.00
avgChange = 0.00

bank_budget_csv = os.path.join(".", "Resources", "budget_data.csv")

with open(bank_budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # and not to print(f"Header: {csv_header}") 

    
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

        if (greatProfit < changeTotal):
           greatProfit = changeTotal
           gProfitDate  = row[0]
        if (greatLoss> changeTotal) :
           greatLoss = changeTotal
           lProfitDate = row[0]

# Set variable and open the output file
output_file = os.path.join("./Resources","Summary.txt")
writer = open(output_file,"w",newline="")


createSummary()




    


 