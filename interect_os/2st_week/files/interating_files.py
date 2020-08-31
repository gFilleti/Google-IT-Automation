#!/usr/bin/env python3.8
import os


os.chdir("base_files")#with this the scrip can work in any OS
path = "long_text.txt"

print('\n----------------------for loop without strip()----------------------------\n')
with open(path) as long_text:
    for line in long_text:
        print(line.upper())

#the long_text has by default a new-line(\n) caracter on the end of each line, so
# the print function print with \n at the and by default tooself.
#this will cause the line jump one line(whitespace), and not keep the text format

print('\n--------------------for loop with a strip()----------------------------\n')
with open(path) as long_text:
    for line in long_text:
        print(line.rstrip().upper())#can use strip() or rstrip()


  #with strip() method we can strip the \n form the line and keep only the new-line
  #of print, wich means now whitespace.

print('\n--------------------reading file into a list----------------------------\n')

file = open(path)

lines = file.readlines()#create a list of string with the lines, here we can see
                        # the new-lines(\n) character in the end of each string
                        # the backslash (\)  indicates that the caracter its not
                        #printable, the name for this is Ecape sequences
                        #other commom escape sequence its \t(tab)
file.close()
lines.sort()#the text will start from the end to the beginning

print(lines)


# the read method or the readlines() method will read the hole file, wich  can
#use alot of computer memory to hold it and lead to poor performance
# if  file has a few kilobys it fine for read and procees completely in memory
#but for large file like a log file of hundreds  of megabytes it more efficient to
#process it line by line
