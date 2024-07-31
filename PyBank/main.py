# Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("..","Starter_Code", "PyBank", "Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip first line (header)
    next(csvreader)
    
    #set variables
    num_of_rows = 0
    total = 0
    max = 0
    min = 0
    max_month = ""
    min_month = ""
    
    #for loop goes through every row in csv file
    for row in csvreader:
        #counts the number of rows
        num_of_rows = num_of_rows + 1
        #adds the total 
        total = total + int(row[1])
        #if statement that checks if each total is the highest yet and if it is sets that row to the highest, saves that rows month as the highest month as well
        if int(row[1]) > max:
            max = int(row[1])
            max_month = row[0]
        ##if statement that checks if each total is the lowest yet and if it is sets that row to the lowest, saves that rows month as the lowest month as well
        if int(row[1]) < min:
            min = int(row[1])
            min_month = row[0]

    #print results to terminal and to text file
    f = open("Financial Analysis.txt", "a")
    print("Financial Analysis")
    f.write("Financial Analysis\n")
    print("-------------------------------")
    f.write("-------------------------------\n")
    print("Total Months: ", num_of_rows)
    f.write("Total Month: " + str(num_of_rows) + "\n")
    print("Total: $", total)
    f.write("Total: $" + str(total) + "\n")
    average = total/num_of_rows
    print("Average Change: $", round(average,2))
    f.write("Average Change: $" + str(round(average, 2)) + "\n")
    print("Greatest Increase in Profits: ", max_month, " ($", max, ")")
    f.write("Greatest Increase in Profits: " + str(max_month) + "($" + str(max) + ")\n")
    print("Greatest Decrease in Profits: ", min_month, " ($", min, ")")
    f.write("Greatest Decrease in Profits: " + str(min_month) + "($" + str(min) + ")\n")
    f.close()
 


