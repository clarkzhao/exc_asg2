#!/usr/bin/python

import sys
pre_word = ""
pre_file_name = ""
sum = 0
for line in sys.stdin:
    line = line.strip()
    word, file_name, value = line.split()
    value = int(value)
    if pre_word == word:
        if pre_file_name == file_name:
            sum += value
        else:
            print ("{0} {1} {2}".format(pre_word, pre_file_name, sum))
            sum = value
            pre_file_name = file_name
    else:
        if pre_word:
            print ("{0} {1} {2}".format(pre_word, pre_file_name, sum))
        pre_word = word
        pre_file_name = file_name
        sum = value

if pre_word == word:
    print ("{0} {1} {2}".format(pre_word, pre_file_name, sum))
