# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

# Set up variables
total_votes = 0
candidate_dict = {}

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:

        # Calculate the total number of votes cast
        total_votes = total_votes + 1

        if (row[2] not in candidate_dict):
        # List of candidates who received votes
            candidate_dict[row[2]] = 1
        else:
             candidate_dict[row[2]] += 1


print("Election Results")
print("------------------------------")
print("Total Votes : " + str(total_votes))
print("------------------------------")
most_votes = 0
for key in candidate_dict:

    print(f"Candidate {key} got" )
    print(f"{candidate_dict[key]} votes, {round((candidate_dict[key]/total_votes)*100)}%")
    print("------------------------------")
    if (candidate_dict[key] > most_votes):
        winner = key
        most_votes = candidate_dict[key]

print(f"{winner} won!")
print("------------------------------")

with open ("PyPollOutput.txt", "w") as textfile:
    textfile.write("Election Results")
    textfile.write("\n")  
    textfile.write("------------------------------")
    textfile.write("\n")  
    textfile.write("Total Votes : " + str(total_votes))
    textfile.write("\n")  
    textfile.write("------------------------------")
    textfile.write("\n")  
    most_votes = 0
    for key in candidate_dict:

        textfile.write(f"Candidate {key} got" )
        textfile.write("\n")  
        textfile.write(f"{candidate_dict[key]} votes, {round((candidate_dict[key]/total_votes)*100)}%")
        textfile.write("\n")  
        textfile.write("------------------------------")
        textfile.write("\n")  
        if (candidate_dict[key] > most_votes):
            winner = key
            most_votes = candidate_dict[key]

    textfile.write(f"{winner} won!")
    textfile.write("\n")  
    textfile.write("------------------------------")