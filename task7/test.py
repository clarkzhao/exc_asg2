#!/usr/bin/python 
import sys
from BloomFilter import BloomFilter
from jhash import jhash_short
import fileinput
def main(num_keys,file_dir):
    input_keys =  int(num_keys)
    bf = BloomFilter(input_keys)
    for line in fileinput.input(file_dir):
        line = line.strip()
        if bf.query(line) == 0:
            bf.insert(line)
            print line
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
