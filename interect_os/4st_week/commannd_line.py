#!/usr/bin/env python3.8

import sys
import os

#Command_line arguments are parameters that are passed to a program when it's started

print(sys.argv) # this will print the command-line arguments that are passed with the program.
                #if we call ./command_line.py it will print the list of commands passed, in this case it self ['./command_line']
                #but we can pass parameter while calling the script. ./command_line.py parameter1, parameter2, paramete3
                # so the script will print a list of all the commands: ['./command_line.py', 'parameter1', 'parameter2', 'paramete3']
                #this parameter can be information we want to pass to our program use  before it even starts.
                #So it lets us create more and more automation.



#Exit status or Return code: its a value returned by a programs to the shell. When a program suceed it return 0 and any other number if it fails.
#the other number are relationated to a diferent erro type. we use bash command $? to print if the command runned successfully.
#For exeemple we can use the WC command which count the number of lines, words and characters in a file. Then use echo $? to check if it succeeded.
#in pyhton we can use:


filename=sys.argv[1]#in this case the frist parameter of sys.argv will be stored as a name of file. so we dont need "to open" the program to executed it;
                    # in other world we use command line parameter to tell our programs what to do without having to interact with them
                    #an use exit values to know if our command suceeeded or failed,
if not os.path.exists(filename):
    with open(filename, "w") as file:#if the name doenst exists a file will be craeted
        file.write("New File Created\n")
else:
    print("Error, the file {} already exists!".format(filename))#if exists a error menssage will be printed
    sys.exit(1)
