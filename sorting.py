"""
Following code access data stored in file 'users.csv'
and sorts them according to a sorting factor stored in variable 'sortingFactor',
which can be changed as per dataset and needs,
and stores the sorted data in a file names 'users-sorted.csv' 
"""

sortingFactor = "UserName"

import csv
import os

if os.path.isfile("users-sorted.csv"):
    os.remove("users-sorted.csv")

sourceFile = open("users.csv")
csvreader = csv.reader(sourceFile)

fields = []
fields = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

countOfRows = len(rows)

sortingIndex = fields.index(sortingFactor)


# Bubble Sort to sort values according to the Sorting Factor
for i in range(0,countOfRows-1):
    for j in range(i+1,countOfRows):
        if rows[i][sortingIndex] > rows[j][sortingIndex]:
            temp = rows[i][sortingIndex]
            rows[i][sortingIndex] = rows[j][sortingIndex]
            rows[j][sortingIndex] = temp


file = open("users-sorted.csv",'w',newline='')
writer = csv.writer(file)
writer.writerow(fields)

for i in range(0,countOfRows):
    writer.writerow(rows[i])

print("User Data Sorted According to",sortingFactor)