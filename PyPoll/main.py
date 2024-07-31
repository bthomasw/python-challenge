# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..","Starter_Code", "PyPoll", "Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip first line (header)
    next(csvreader)

    #list that will store each unique name
    list_of_unique_names = []
    #seperate list that will store a count of each unique name
    count_of_unique_names = []
    #variable for number of rows or total votes
    num_of_rows = 0

    #for loop that goes through every line in csv file
    for row in csvreader:
        #counts total votes
        num_of_rows = num_of_rows + 1

        #checks if the name has been used before, if it has do nothing, if it hasn't add that name to the unique names list and add a cooresponding count varable to the count list
        if row[2] in list_of_unique_names:
            pass
        else:
            list_of_unique_names.append(row[2])
            count_of_unique_names.append(0)

        #check each name in list and if this row equals a name add 1 to the count in the cooresponding count list
        for i, name in enumerate(list_of_unique_names):
            if row[2] == list_of_unique_names[i]:
                count_of_unique_names[i] = count_of_unique_names[i] + 1
    
    
    #print results and create a text file to write to
    f = open("Election Results.txt", "a")    
    print("Election Results")
    f.write("Election Results\n")
    print("----------------------------------")
    f.write("----------------------------------\n")
    print("Total Votes:", num_of_rows)
    f.write("Total Votes:")
    f.write(str(num_of_rows))
    f.write("\n")
    print("----------------------------------")
    f.write("----------------------------------\n")
    
    #variables to use to find who has the most votes and their name
    highest_value = 0
    winner_name = ""

    #for loop to go through every name in list of unique names and print the cooresponding count in the count list
    for i, name in enumerate(list_of_unique_names):
        print(name, ": ", round((count_of_unique_names[i]/num_of_rows) * 100, 3), "% (", count_of_unique_names[i], ")")
        f.write(str(name) + ": " + str(round((count_of_unique_names[i]/num_of_rows) * 100, 3)) + "% (" + str(count_of_unique_names[i]) + ")\n")
        #If statement to compare the vote counts of names and replace the highest with the new highest
        if count_of_unique_names[i] > highest_value:
            highest_value = count_of_unique_names[i]
            winner_name = name

    #countiue printing and writing to text file 
    print("---------------------------------")
    f.write("---------------------------------\n")
    print("Winner: ", winner_name)
    f.write("Winner: " + str(winner_name) + "\n")
    print("---------------------------------")
    f.write("---------------------------------")
    f.close()

    
    
    