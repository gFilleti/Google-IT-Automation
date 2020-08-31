#!/usr/bin/env python3.8

print("This will be printed in the terminal screen if  its not redirected with >  ( redirect but overright) >> ( redirect and append)")

#by default the input is provided bt the keyboard in texxt terminal in  all OS. And the output  and error are shown on the screen
# This aply  for Python scripsts  and all syste commands
# we can change this default  using redirection, wich is  the process of sending a stream to a different destination
# ./stdout_exemple.py  will print in the screen
# ./stdout_exemple.py > new_file.txt this will run the file and redirect to a file called new_file.txt
#if the file doesn't exists it's created
#Each time we perfom a redirection of STDOUT the destination is overwritten, for append we can use >> 

data = input("This will come fron STDIN: ")

print("\nNow we write to STDOUT: " + data)

# in this second exemple its to use ./stdout_exemple < new_file.text on terminal
# Now we can redirect the contets of our  new_file to this script using <
#the file contents will enter as  input to data variable, but  as it was read out side it will not print  the  input
# this happen becous the input was read from a file
# so the data value will only appear in the  STDOUT portion (print  function)

raise ValueError("Now We generate an error to STDERR")
# we can redirect the error (STDERR) to a file with 2>

#./stdout_exemple 2> error_file.txt in tis case we need enter the input

#./stdout_exemple < new_file.txt 2> error_file.txt in tis case the input  it the ne w_file content 
