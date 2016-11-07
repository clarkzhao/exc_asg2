import sys
import random
import math
from HashFunction import HashFunction


class BloomFilter():
    '''
    number_of_keys: 
    	sotores the number of lines while maintaining the error_rate 

	error_rate:
		The false-positive probability p
		the default error_rate is 0.001

    '''
    
    def __init__(self, num_keys, error_rate = 0.001):
    	self.num_keys = num_keys
    	self.error_rate = error_rate
    	self.num_hashes = int(math.ceil(math.log(1.0/error_rate,2)))
    	self.num_bits = int(math.ceil(num_keys * abs(math.log(error_rate,2)))/math.log(2))
    	self.bit_array = [0]* self.num_bits
    	self.hashFunctions = []
    	for i in range(0, self.num_hashes):
            hash_obj = HashFunction(self.num_bits)
            obj = self.hashFunctions.append(hash_obj)
    def insert(self, key):
        i = 0
    	for func in self.hashFunctions:
            i += 1
            hash = func.get_value(key)
            index = int(hash)
            #print "Hash is " + str(hash) + " Index is " + str(index)
            self.bit_array[index] = 1

    def query(self, key):
    	result = True
    	for func in self.hashFunctions:
            index = int(func.get_value(key))
            result = result * self.bit_array[index]
        return result

    def show(self):
    	print "number of keys: {0}".format(self.num_keys)
    	print "error rate: {0}".format(self.error_rate)
    	print "number of hashes: {0}".format(self.num_hashes)
    	print "number of bits: {0}".format(self.num_bits)
    	print "number of bits per key {0}".format(self.num_bits/self.num_keys)

