#!/usr/bin/env python
import sys
 
resultant_dictionary = {}
 
# getting input from sys.stdin

for every_line in sys.stdin:
    value = every_line.strip().split()

#if it exists in dictionary simply append it else create a new key valu pair.

    if (value[0] in resultant_dictionary): 

        resultant_dictionary[value[0]].append(value[1])

    else:

        resultant_dictionary[value[0]] = [value[1]]

#printing key and its length i.e count of frnds

for key in resultant_dictionary:

    print key, len(resultant_dictionary[key])
