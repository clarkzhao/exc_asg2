#!/usr/bin/python

import sys
import os
for line in sys.stdin:                  # input from standard input
    line = line.strip()
    file_name = os.environ['mapreduce_map_input_file'].split('/')[-1]
    tokens = line.split()
    for token in tokens:
        print ("{0}\t{1}\t{2}".format(token, file_name, 1))
