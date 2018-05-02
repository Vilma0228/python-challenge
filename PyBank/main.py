import os
import csv

#Files to load

PyBankpath = "budget_data_1.csv"

#Read the csv and convert to dictionaries
with open (PyBankpath) as revenue_data:
    reader = csv.reader(revenue_data)

    #Use the next to skip first title row
    next (reader)
    revenue = []
    date = []
    rev_change = []

    #Loop to generate sum of column 1
    for row in reader:
        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))

 #Loop total of difference between all row of column "Revenue" and found Total Revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

# Also found out max revenue change and min revenue change. 
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


print("Avereage Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


    