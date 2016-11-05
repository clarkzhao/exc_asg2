#!/usr/bin/python
import sys

acc_anws = []
for line in sys.stdin:
    line = line.strip()
    #anw is the anser Id, first is the user id or the notation of 'ANS'
    first, anw= line.split()
    #The output of the mapper is sorted, so the first part of the output starts with first key 'ANS', those vaulues of accepted anwser ID is sotred at first.
    if first == 'ANS': 
        acc_anws.append(anw)
    #The following is all the answer Id and if it is accepted, print the filtered result.
    else:
        if anw in acc_anws:
            print ("{0} {1}".format(first,anw))
