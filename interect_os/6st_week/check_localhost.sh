#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "ERROR! 127.0.0.1 is no in /etc/hosts"
fi
#finish

# in bash  scripting, the condition used is based on the exit status of commands
#In bash scripiting, an exit value of 0 mens sucess
# to create a conditional expression, we're going to call a command an if the exit status of that command it zero,
#then the condition will be considered true
#this logic is used by the if operator in bash

# the indentation its a style choice, but it not mandatory in Bash

# the if bloch start in ; then and finishes in fi

# the grep command called by our script search the correspondent line in the file ans exit with the value

#Test is a comand that evaluates the conditions received and exits with zero when they'are tru and with one when they're false

 if test -n "$PATH"; then echo "Your path is not empty"; fi

 if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

# [ ] its an alias for test, for use this alias there needs to be a space before the closing bracket
