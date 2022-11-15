import csv

# Accessing the csv file
sourceFile = open("users.csv")
csvreader = csv.reader(sourceFile)

# getting header of the csv file
fields = []
fields = next(csvreader)

# getting all data vales in form of list
rows = []
for row in csvreader:
    rows.append(row)

countOfRows = len(rows)


# Taking username as input from user to get details 
print("Enter username to get details: ",end="")
username = input()



print("\n ----------User Details---------- ")
for i in range(0,countOfRows):
    if rows[i][fields.index("UserName")] == username:
        for j in range(len(fields)):
            print(fields[j] + ": " + rows[i][j])
        break