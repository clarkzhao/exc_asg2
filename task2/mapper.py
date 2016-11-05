#!/usr/bin/python

import sys
import os

for line in sys.stdin:
    line = line.strip()
    tokens = line.split() 
    post_typeId = tokens[2]
    if post_typeId.split('=')[-1] == '"1"':
        Id = tokens[1]
        Id_num = int(Id.split('=')[-1].split('"')[1])
        view_count = tokens[6] if tokens[6].split('=')[0] == 'ViewCount' else tokens[5]
        view_count_num = int(view_count.split('=')[-1].split('"')[1])
        print ("{0} {1}".format(Id_num, view_count_num))
