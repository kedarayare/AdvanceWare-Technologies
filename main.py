import requests
import csv
import time

# RANDOM USER DATA API URL
URL = "https://random-data-api.com/api/v2/users"


# User data fields needed to be stored in the csv
header = ['id', 'FirstName','LastName','UserName','Email','Avatar','Gender','DoB','Address']
fields = ['id', 'first_name','last_name','username','email','avatar','gender','date_of_birth','address']


# Function to convert address from dict to string
def addressField(data):
    addressString = ""
    for key, value in data.items():
        if key == "coordinates":
            break
        # print(type(value))
        addressString += value + ","
    return addressString[0:-1]


file = open("users.csv",'w',newline='')
writer = csv.writer(file)

# Comment out the below line if the CSV file already has header added
writer.writerow(header)
rowCount = 0


# While loop to get data values from the URL after every 1 second
while(True):
    r = requests.get(url=URL)
    userData = r.json()
    row = []

    # Looping through only required fields to be stored in csv
    for field in fields:
        if field == "address":
            row.append(addressField(userData[field]))
        else:
            row.append(userData[field])

    
    writer.writerow(row)
    
    # rowCount variable to keep a track of data rows added to the csv file
    rowCount += 1

    print()
    print("Data Received: ")
    print("Total Rows: ", rowCount)
    
    time.sleep(1)
    


