import os
import csv

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
cand={} #Initializate an empty dictionary

with open(csvpath, newline='') as csvfile:

    Poll = csv.reader(csvfile, delimiter=',') # First we read the file and eliminate the header
    csv_header = next(Poll)

    for row in Poll: # With this for we search in the csv file
        if row[2] not in cand:
             cand[row[2]]=1 # If the name of the candidate is not in the dictionary we add it
        else:
            cand[row[2]]+=1 # If the name is alredy there we add 1 vote to the candidate.

    Total=sum(cand.values()) # We save the total number of votes.
            
    print("Election Results")
    print("Total Votes: {Total}")
    print("-------------------------")
    
    for x,y in cand.items(): # With this for we print each candidate and it's respective number
        print(f"{x}: {round(y/Total*100,2)}% ({y})")   # of votes

    print("-------------------------")
    print(f"Winner: {max(cand,key=cand.get)}")
    print("-------------------------")

#We also generate a text file named PyBank were we save this info:
file1 = open("PyPoll.txt","w")
file1.write("Election Results\n")
file1.write("Total Votes: \n")
file1.write("-------------------------\n")
for x,y in cand.items():
        file1.write(f"{x}: {round(y/Total*100,2)}% ({y})\n")
file1.write("-------------------------\n")
file1.write(f"Winner: {max(cand,key=cand.get)}\n")
file1.write("-------------------------")
file1.close()
