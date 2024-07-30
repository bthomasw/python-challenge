import pandas as pd
def print_percentage_of_votes(df, unique_value, total):
    new_df = votes[votes['Candidate'] == unique_value]
    new_df = new_df.reset_index(drop = True)
    rows, columns = new_df.shape
    percentage = rows/total
    print(new_df.iloc[0, 2], ": ", round((percentage * 100),3), "% (", rows, ")")

def get_winner(df, unique_value):
    new_df = votes[votes['Candidate'] == unique_value]
    new_df = new_df.reset_index(drop = True)
    rows, columns = new_df.shape
    return rows

votes = pd.read_csv('C:/Users/thoma/Classwork/Week 3/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv')
rows, columns = votes.shape
print("Total Votes:", rows)
unique_values = votes['Candidate'].unique()
num_unique = unique_values.size



for unique in range(num_unique):
    print_percentage_of_votes(votes, unique_values[unique - 1], rows)

highest_value = 0
unique_index = -1
for unique in range(num_unique):
    new_value = get_winner(votes, unique_values[unique - 1])
    if new_value > highest_value:
        highest_value = new_value
        unique_index = unique - 1
print("Winner: ", unique_values[unique_index])



    
    