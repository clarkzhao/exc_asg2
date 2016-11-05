#!/usr/bin/python

import sys
#A dictionary to store the information like {(d2.txt,1), ... , (d5.txt,2)}
i = 0
print "#Count Id"
for line in sys.stdin:
    line = line.strip()
    Id, view_count = line.split()
    if i < 10:
        print Id, view_count 
    i += 1
