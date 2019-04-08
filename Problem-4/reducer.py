#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

friends_dict = {}



for line in sys.stdin:
   
    line = line.strip()
    tokens = line.split(", ")

    tokens[0] = tokens[0].strip("[")
    tokens[0] = tokens[0].strip("\"")

    tokens[1] = tokens[1].strip("]")
    tokens[1] = tokens[1].strip("\"")
    
    if tokens[0] not in friends_dict.keys():
        friends_dict[tokens[0]] = [tokens[1]]
    else:
        friends_dict[tokens[0]].append(tokens[1])


dict2 = friends_dict.copy()

list1 = friends_dict.keys()


for i in list1:
    for j in friends_dict[i]:
        if j in list1:
            if i in friends_dict[j]:
                friends_dict[j].remove(i) 
                friends_dict[i].remove(j)

for k in friends_dict.keys():
    for l in friends_dict[k]:
        print [l, k]
        print [k ,l]            
