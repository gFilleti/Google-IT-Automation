#!/usr/bin/env python3.8
print("\n-------------subprocess Run function------------------------------\n")

print("this module has fuction to execute subprocesses by commands\n")
import subprocess

print("\n-------------subprocess date------------------------------\n")

date = subprocess.run(["date"])#subprocess that show the current day

print(date)#will print an object which says the command used and the exit status


print("\n-------------subprocess sleep------------------------------\n")

sleep =subprocess.run(["sleep", "2"])#the sleep command, which waits for a number of seconds before running.
print("the srcipt waited 2 seconds before printing this string")
print(sleep)#will print an object which says the command used and the exit status


# the parent processe its the python script and when the codes executes it creates a chield process that will run  in a secondary  environment
#while the parent process stay blocked until the subprocess its finished

# In other words the run function return an object of the completed porcess type. This object includes information related to execution of the command.
#To run the external command a secondary enviromment its crated for the chield process or a subprocess where the  command is executed.
#While the parent process, which is our script, is waitting on the subprocess to finished.

print("\n-------------subprocess showing exit status------------------------------\n")

result = subprocess.run(["ls", "this_file_does_not_exist"])# the .run  will run the bash command ls but try to list a file that soes not exist
print("exit status: {}".format(result.returncode))
#here we will print only returncode of the returned object, which its the exit status(0 if the command runned or a number if it had an error)
#If the returned number of returncode its diferent of zero so theres ocurred an error, the number it the error type.
# in this case will return 2 which is => ls: cannot access 'this_file_does_not_exist': No such file or directory

# Uselly we just store the command in a variable for priting command that it inportant to show the result as changing the premitions of a bunh of files
#as using subprocess.run(["chmod"], "777")

#return code its  the same as exit status.

print("\n-------------subprocess host------------------------------\n")

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)#host command converts a host name to an IP adress amd vive versa.
                                                                 # passing the parameter capture_output equals true for we can acess it in a variable
                                                                 #using .stdout atribute
                                                                 #the result variable is a completed process instance that we can access after the code execute

print("exit status: {}\n".format(result.returncode))

print("STDOUT UTF-8 not decoded: {}\n".format(result.stdout))
# we can print an operate with the output generated by the comman, which is stored in the stdout attribute of the object
#b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'  the b in the beginning tell us that  te string
#is not a proper string for python., becouse its in UTF-8, but Python string are Unicode

#Since Python 3.0, the language’s str type contains Unicode characters, meaning any string created using "unicode rocks!",
#'unicode rocks!', or the triple-quoted string syntax is stored as Unicode.
# so in python 3 all strings are Unicode

#for decode from UTF-8 to Unicode we use decode method. This method applies an enconding to transfrom the bytes into a string.


print("STDOUT UTF-8 decoded: {}".format(result.stdout.decode().split()))
