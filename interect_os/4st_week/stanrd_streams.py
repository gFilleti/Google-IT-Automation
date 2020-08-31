#!/usr/bin/env python3.8
print("\n--------------------------I/O STREAMS--------------------------------\n")

data = input("This will come from STDIN: ")# standard input its a  channel between a program and a source of input.
                                           #Usually in the form of text data from keyboard;

print("Now we write it to STDOUT: " + data)# STDOUT its a patway between a program an a target of output
                                           # standard output genarally takes the form of txt displayed in a terminal

print("Now we generate an error to STDERR: "+ data +1)#standard error or STDERR, it displays output error,
                                                      #showing error menfages and diagnostics fromthe program.
