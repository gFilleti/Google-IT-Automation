#!/bin/bash

n=1
while [ $n -le 5 ]; do # the loop starts with the do keyword
  echo "Iteration number $n"
  ((n+=1))
done #and the loop fineshes with the done keyword

#the [ $n -le 5 ] check if the variable N is less than or equal to five using the -le(lessequal) operator
