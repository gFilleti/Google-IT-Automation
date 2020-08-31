#!/usr/bin/env python3.8

import os

print("HOME: " + os.environ.get("HOME", ""))

print("SHELL: " + os.environ.get("SHELL", ""))

print("FRUIT: " + os.environ.get("FRUIT", ""))#there no Fruit enviroment variable in the shell, but we can create it with a bash command export
                                              # export FRUIT=Pineapple

#os.environ return a dictionary with the enviroment variable
#with the .get method it will try search the key (frist parameter) except I will display a defined output (second parameter)
