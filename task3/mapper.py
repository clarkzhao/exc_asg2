#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    tokens = line.split() 
    post_typeId = tokens[2] #The postTypeId is always in the third position

    #When it's a question, print the accepted answer Id
    if post_typeId.split('=')[-1] == '"2"':
        Id = tokens[1]
        Id_num = int(re.findall(r'\d+',Id)[0])
        for token in tokens:
            if re.search("OwnerUserId",token):
                owner_user_id = token
                owner_user_id_num = int(re.findall(r'\d+',owner_user_id)[0]) 
                break
        #<owner user id, anwser id> is the output
        print ("{0} {1}".format(owner_user_id_num, Id_num))
