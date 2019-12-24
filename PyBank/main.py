import os
import csv

csvpath = os.path.join('Resources', 'PyBank_Data.csv')
BankData=[1,0,0,0,0,0] # [months,profit total,max profit, max lost,profit change,proft avg]
date=[0,0] # [Date of max profit, Date of max lost]

temp=0 # Temporal variable to store the proft/lost from the last month

with open(csvpath, newline='') as csvfile:

    Bank = csv.reader(csvfile, delimiter=',') # First we read the file and eliminate the header
    csv_header = next(Bank) 
    # We initializate some variables using the information provided from the rist row
    t=next(Bank)
    date[0]=t[0]
    date[1]=t[0]
    BankData[1]+=int(t[1])
    temp=int(t[1])
    # ----------------------------
    for row in Bank: # We start going through the csv file
        
        BankData[0]+=1 # Increment a month. From inspecting the file we know each row is a month
        BankData[4]=int(row[1])-temp # Here we store the profit/lost change
        BankData[5]+=BankData[4] # We add all the profit/lost change, in the last step we're going to use it to know the average.
        temp=int(row[1]) # We save the profit/lost value from this month to compare it to next month
        BankData[1]+=temp # We also add this value to the total.
        if BankData[4]>BankData[2]:  # This conditional is to save the value and date of the best profit change
            BankData[2]=BankData[4]
            date[0]=row[0]
        elif BankData[4]<BankData[3]: # This conditional is to save the value and date of the worst profit change
            BankData[3]=BankData[4]
            date[1]=row[0]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {BankData[0]}")
    print(f"Total: {BankData[1]}")
    print(f"Average  Change: ${round(BankData[5]/(BankData[0]-1),2)}") #Here we do a operation to calcute the average, also to round it to 2 decimals
    print(f"Greatest Increase in Profits: {date[0]} (${BankData[2]})")
    print(f"Greatest Decrease in Profits: {date[1]} (${BankData[3]})")

# We also generate a text file named PyBank were we save this info:    
file1 = open("PyBank.txt","w")
file1.write("Financial Analysis\n")
file1.write("----------------------------\n")
file1.write(f"Total Months: {BankData[0]}\n")
file1.write(f"Total: {BankData[1]}\n")
file1.write(f"Average  Change: ${round(BankData[5]/(BankData[0]-1),2)}\n") #Here we do a operation to calcute the average, also to round it to 2 decimals
file1.write(f"Greatest Increase in Profits: {date[0]} (${BankData[2]})\n")
file1.write(f"Greatest Decrease in Profits: {date[1]} (${BankData[3]})")
file1.close()
