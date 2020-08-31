#!/bin/bash

line="-----------------------------------------------------------------------" #bash variable must not have space at on side or the other
                                                                               # if have space line = "something" the show will complain that it can't find
echo "Staring at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"; echo $line

# tree commands: uptime , free and who
#echo command to print some more information and make the output more readable by living empty line between the commands
# the dolar sing parentesis $(command) indicate that the output of the command should be passed to echo command
#and be printed to the screen
#in this case echo will print the current date
echo "Python scripts:"; echo *.py; echo $line

echo "Text files with five character in the name:"; echo ?????.txt

#glob are character that allow to create list of files
# the star * and the question mark ? are the most common globs
