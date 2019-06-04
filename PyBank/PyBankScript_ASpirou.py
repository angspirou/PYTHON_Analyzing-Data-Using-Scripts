# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Set up variables
total_months = 0 
months = []
total_net = 0
previous_value = 0
revenue_list = []
max_list = ["", 0]
min_list = ["", 99999999]

print("Financial Analysis")
print("-------------------------------------")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)


    row = next(csvreader)
    total_net = total_net + int(row[1])
    total_months = total_months + 1
    previous_value = int(row[1])

    for row in csvreader:

        # Calculate the total amt of months:
        total_months = total_months + 1
        
        # Calculate the total amt of Profits/Losses:
        total_net = int(row[1]) + total_net 

        # Calculate the average change in Profit/Losses:
        revenue_change = int(row[1]) - previous_value 
        previous_value = int(row[1])
        revenue_list = revenue_list + [revenue_change]
        months = months + [row[0]]

        # Find max & min with output showing months the $ corresponds to:
        if revenue_change > max_list[1]:
            max_list[0] = row[0] 
            max_list[1] = revenue_change
        if revenue_change < min_list[1]:
            min_list[0] = row[0]
            min_list[1] = revenue_change     
revenue_avg = sum(revenue_list) / len(revenue_list)

print("Total Months : " + str(total_months))
print("Total : $" + str(total_net))
print("Average Change : $" + str(revenue_avg))
print("Greatest Increase in Profits : " + str(max_list[0]) + "(" + str(max_list[1]) + ")")
print("Greatest Decrease in Profits : " + str(min_list[0]) + "(" + str(min_list[1]) + ")")

# Create text file output
with open ("PyBankOutput.txt", "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n")  
    textfile.write("-------------------------------------")
    textfile.write("\n")  
    textfile.write("Total Months : " + str(total_months)) 
    textfile.write("\n")  
    textfile.write("Total : $" + str(total_net))
    textfile.write("\n")
    textfile.write("Average Change : $" + str(revenue_avg))
    textfile.write("\n")
    textfile.write("Greatest Increase in Profits : " + str(max_list[0]) + "(" + str(max_list[1]) + ")")
    textfile.write("\n")
    textfile.write("Greatest Decrease in Profits : " + str(min_list[0]) + "(" + str(min_list[1]) + ")")






        


