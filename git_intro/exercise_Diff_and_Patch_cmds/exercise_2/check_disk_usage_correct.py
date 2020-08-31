#!/usr/bin/env python3.8
"""The script below fix return bug but  still has some bugs"""
import shutil
import sys

def check_disk_usage(disk,min_absolute,min_percent):
    """"Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


#Check for at least 2 GB and 10% percent_free
#if not check_disk_usage("/", 2*2**30, 10): the function paramter 2**30
#its converting for a second time, frist was made in gigabytes_free.
if not check_disk_usage("/", 2, 10):
    print  ("ERROR: Not enough disk space")
    #return 1 doesnt work out of a function, for sending out without a function
    #we can use sys.exit, exit code of the script
    sys.exit(1)

print("Everthing ok")
sys.exit(0)
