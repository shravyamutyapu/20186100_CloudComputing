#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

dictionary_1 = {}


# input comes from STDIN
for line in sys.stdin:
    
    line = line.strip()
    tokens = line.split(", ")

    tokens[0] = tokens[0].strip("[")
    tokens[0] = tokens[0].strip("\"")

    tokens[1] = tokens[1].strip("]")
    tokens[1] = tokens[1].strip("\"")
    
    if tokens[0] not in dictionary_1.keys():
        dictionary_1[tokens[0]] = tokens[1][0:-10]

# print dictionary_1
listOfKeys = list(dictionary_1.keys())
listOfValues = list(dictionary_1.values())

updated_list = set(listOfValues)
for i in updated_list:
    print "\""+i+"\""



