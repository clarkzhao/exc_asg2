from jhash import jhash_short
import random

class HashFunction():
    def __init__(self, num_bits):
        self.num_bits = num_bits
        self.a = random.randint(0,self.num_bits) 
        self.b = random.randint(0,self.num_bits)
    def get_hash(self,key):
        return jhash_short(key)
    
    def get_value(self,x):
        return (self.a*self.get_hash(x) + self.b) % self.num_bits
