#!/usr/bin/python

import sys
outputs = []
pre_word = ""
def printlis(lis):
    return '{' + ', '.join(lis)+ '}'
for line in sys.stdin:
    word, file_name, value = line.split()
    files = ', '.join(['('+file_name, value+')'])
    if pre_word == word:
        outputs.append(files)
    else:
        if pre_word:
            print ("{0}: {1} : {2}".format(pre_word, len(outputs), printlis(outputs)))
        pre_word = word
        outputs = [files]
if pre_word == word:
    print ("{0}: {1} : {2}".format(pre_word, len(outputs), printlis(outputs)))
