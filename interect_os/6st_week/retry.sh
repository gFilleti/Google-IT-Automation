#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
  sleep $n
  ((n=n+1))
  echo "Retry #$n"
done;

#$1 it's equal to sys.argv[1] of python. This what we use to access the frist command line argument
#we store the parameter in a variable called command an then we execute the while loop
#until either the command succeeds otr the end variable reaches a value of five
# the sleep command its used by preventing a falling due to CPU usage, network or resource exhaustion.
#So it makes the script wait a bit before trying again

#./retry.sh ./random-exit.py this bash scrip will use the python scrip as input to the command variable
#So each time i will keep executing the python script as command uitl five times
