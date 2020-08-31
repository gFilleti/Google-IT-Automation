#!/usr/bin/env python3.8

import csv


employee = [
["Alex Vance", "7384-4355-3245", "Liberty Figther"],
["Gordon Freeman", "2345-4562-4245", "Dam Good Fighter"],
["Dr.Eli Vance", "3432-5434-5422", "Incredable Scintist"],
["Dr.Elizath Chon", "3456-6557-3536", "Vice Scientist"]
]

print("\n--------------------------------CREATING CSV FILE----------------------------\n")

print("employees:{} ".format(employee))


with open('employees.csv', 'w') as employee_csv:
    writer =csv.writer(employee_csv)#the writer variable its now a instace of CSV class, same as defeing this variable as an object of class writer
    writer.writerows(employee)#we can use .writerow with will write one row ate the time
                           #or use .writerows witch will write all of them together
print("CSV file was created")


print("\n--------------------------------READING CSV FILE----------------------------\n")

f = open("employees.csv")

csv_read = csv.reader(f)

for row in csv_read:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))


print("\n---------------------------------------END------------------------------------\n")
