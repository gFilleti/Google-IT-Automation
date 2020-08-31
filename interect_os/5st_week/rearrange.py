#!/usr/bin/env python3.8
import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        if name == "":
            print("edge case")
            #this test its a Edge case, Edge cases are imputs to our code that produce unexpected results, and are found at the extreme ends of the ranges
            #of  input we imagine our programs will typically work with
        else:
            print(name)
        return name
    print("{} {}".format(result[2], result[1]))
    return "{} {}".format(result[2], result[1])
