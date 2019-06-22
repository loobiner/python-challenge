#PyBank


import os
import csv

budgetdata = "C:\\Users\\loobi\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\budget-data.csv"

with open(budgetdata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#taking out the header row
csv_header = next(csvfile)

months = [] #to create a list from the months column
profandloss = [] # to create a list from the profit and loss column
differences = [] # to create a list of differences between an index in the profandloss list and its preceding index


for row in budgetdata: # for loop to populate months list and profandloss list
    months.append(row[0])
    profandloss.append(int(row[1])

for i in profandloss: # for loop to populate differences list
    differences.append(int(profandloss[i]) - int(profandloss[i-1]))

jump = differences.index(max(differences)) #to select the months that correspond with 
fall = differences.index(min(differences)) #the min and max values of the difference list
bestmonth = months.index(jump)
worstmonth = months.index(fall)

#printing the summary
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(len(months)))
print("Net Revenue: $"  + str(sum(profandloss)))
print("Average Change: $" + str(sum(differences)/(len(differences)))
print("Greatest Increase in Profits: " + str(bestmonth) + " $" + str(max(differences)))
print("Greatest loss in Profits: $" + str(worstmonth) + " $" + str(min(differences)))



