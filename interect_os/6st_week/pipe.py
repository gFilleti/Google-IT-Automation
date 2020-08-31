#!/usr/bin/env python3.8

import sys

for line in sys.stdin:
    print(line.strip().capitalize())

# we can redirect using pipes |
# cat haiku.text | capitalize.py
# cat command  send the content of the file to standard output, wich we redirect to your script using a pipe
#the sys stdin file object iterate through each line of standard input (in this case the haiku.txt)
#than print the capitalized version to standaerd output
