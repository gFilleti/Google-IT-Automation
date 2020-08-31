#!/usr/bin/env python3.8
import csv


print("\n----------------------------CREATING CSV FILE FORM A DICTIONARY----------------------\n")

users= [
{"name": "Alex Vance","username": "Honney", "phone": "7384-4355-3245", "role": "Liberty Figther"},
{"name": "Gordon Freeman","username": "CrowBar", "phone": "2345-4562-4245", "role": "Dam Good Fighter"},
{"name": "Dr.Eli Vance", "username": "DOCLI","phone": "3432-5434-5422", "role": "Incredable Scintist"},
{"name": "Dr.Elizath Chon", "username": "CHONCHON", "phone": "3456-6557-3536", "role": "Vice Scientist"}
] #list of dictonerys we want to be write in the file

keys = ["name", "username", "phone", "role"]#difine the list of keys , this will be the columns names

with open('departament.csv', 'w') as departament: #open the filefor writing, if doesnt exists the file will be crated  if exists the contents will be overwritten
    writer = csv.DictWriter(departament, fieldnames=keys)
    #generates a CSV file form the contents of a list od dictionaries
    #this means that each element in the list will be a row in the file,
    #and the values of each field will como out of each of the dictionaries
    #for this to work we have to pass a list of the keys we want to be stored in the file
    writer.writeheader()# this method will create the frist line of the CSV based on the keys : name, username, phone, role (keys as row)
    writer.writerows(users)# and this method will turn the lines of dictionaries into rowns in that file: Gordon Fremman, CrowBar, 234...etc

print("the list of dictionaries is\n"
"{}".format(users))



print("\n----------------------------REDING CSV FORM A DICTIONARY----------------------\n")

with open('departament.csv') as departament:
    reader = csv.DictReader(departament)
    # this reader turns each row of the data in a CSV file into a DICTIONARY
    #then we can access the data using the columm names isntead of the position in the row
    #the order of the fields in the file doesn't matter, we just use the name of the field isntead
    for row in reader:
        print(("{} username is {} and the role is {}").format(row["name"], row["username"], row["role"]))

print("\n-----------------------------------------END-------------------------------------\n")
