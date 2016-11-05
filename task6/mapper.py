#!/usr/bin/env python
import sys
import random
line_number = 0 #line number starts from 0
k = 100 #the total number of samples
resevoir = []
for line in sys.stdin:
    if line_number < k:# The resevoir has elements of [0,1,...,k-1] and k samples in total
        resevoir.append(line.strip())
    else:
        j = random.randint(0,line_number) #j is selected randomly from range of [0,n] where n is current line number
        if j < k: # the probability of selection is k/n, n is the current line numbers
            resevoir[j] = line.strip()
    line_number += 1
for item in resevoir:
    print item
