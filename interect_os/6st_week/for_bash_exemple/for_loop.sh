#!/bin/bash

for file in *.HTM; do
  name=$(basename "$file" .HTM)
  mv "$file" "$name.html"
done
#$(command) will call the comman an keep the output
#the "$file" the double-quotes take of any spaces ( like strip() in python), so this will make the command works even the file come with spaces.
#using double-quotes in Bash sxripts when dealing with files names or any variable taht could include spaces is a good practice
# in bash scripts that modifies the files in your system, it good to test first by printing with echo the change
#echo mv "$file" "$name.html", this will print the new name instad of modify it, it the script work as aspected  so we can take of the echo from the line
# its allways a good idea frist eun the sxript without actually modifying te file system. This will catch any possible buff that the script might have
