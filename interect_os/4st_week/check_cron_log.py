#!/usr/bin/env python3.8

import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        print(line.strip())
        print(result[1],'\n')
print(usernames)

"""
The server that generates this log file has been acting strangely and
we suspect it's due to a Cron job started by one of the system administrators.
You may remember that Cron jobs are used to schedule scripts on UNIX-based operating systems.
To find out what's happening with the server, we want to audit the log files and see
exactly who's been launching CRON jobs.
By looking at the sample log, we can see that the lines that'll be most interesting to
us are the ones that contain the Cron substring. These lines also show the user who
started the Cron job wrapped in parentheses. With this info, we can ignore any line without the Cron substring in it.
We can check for this using the "in" keyword.
"""
