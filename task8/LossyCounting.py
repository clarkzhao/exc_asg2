#!/usr/bin/python 
class LossyCounting(object):
    '''
        N: 
            the number of elements
        s:
            support threshold
        eps:
            error, 10% of s
        items:
            a dictionary stores the stream data element
        buckets: 
            a dictionary stores the buket value
        b_current:
            the current bukey value = N/w where N starts from 1and increases            by 1 and w is the bucket width 1/eps

    '''
    def __init__(self,s):
        self.N = 1
        self.s= s
        self.eps = s*0.1
        self.w = 1/self.eps
        self.items = {}
        self.buckets = {}
        self.b_current = 1
        
    def add(self, item):
        self.N += 1
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
            self.buckets[item] = self.b_current - 1
        
        if self.N % int(1 / self.eps) ==0:
            for item in self.items.keys():
                if self.items[item] <= self.b_current - self.buckets[item]:
                    del self.items[item]
                    del self.buckets[item]
            self.b_current += 1
    def getCount(self):
        threshold_count = self.s * self.N
        for item in self.items.keys():
            if self.items[item] <= self.b_current - self.buckets[item]:
                del self.items[item]
                del self.buckets[item]

        for item in self.items:
            if self.items[item] >= threshold_count - self.eps * self.N:
                yield (item, self.items[item])

if __name__ == '__main__':
    import sys
    counter = LossyCounting(0.01)
    
    for line in sys.stdin:       
        line = line.strip()
        counter.add(line)
    
    for item, count in sorted(counter.getCount(), key= lambda x:x[1]):
        print item, count

