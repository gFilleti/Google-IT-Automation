#!/usr/bin/env python3.8
import os

print("-----------------------Current Work Directory-------------------------------")

print(os.getcwd())

print("\n-----------------------Make New Directory-------------------------------")

os.mkdir("new_dir") #creates  a new Directory
print("\n The Directory new_dir was created")

print("-----------------------Change  Directory-------------------------------")

os.chdir("new_dir")#can be used realative or absulute paths as parameter
print("\n The Directory was changed to new_dir")

print("-----------------------Delete  Directory-------------------------------")

os.rmdir("new_dir")#can be used realative or absulute paths as parameter
print("\n The Directory new_dir was deleted")

print(os.getcwd())
print("\n")
