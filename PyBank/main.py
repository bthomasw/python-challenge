import pandas as pd
budget = pd.read_csv('C:/Users/thoma/Classwork/Week 3/python-challenge/Starter_Code/PyBank/Resources/budget_data.csv')
print(budget.head())
rows, columns = budget.shape
print("Total Months:", rows)
total = 0
for ind in budget.index:
    total = total + budget['Profit/Losses'][ind]
print("Total: $",total)
average_change = total/rows
print("Average Change: $", round(average_change, 2))
max_index = budget['Profit/Losses'].idxmax()
print("Greatest Increase in Profits: ", budget['Date'][max_index], "($", budget['Profit/Losses'][max_index], ")")
min_index = budget['Profit/Losses'].idxmin()
print("Greatest Decrease in Profits: ", budget['Date'][min_index], "($", budget['Profit/Losses'][min_index], ")")

