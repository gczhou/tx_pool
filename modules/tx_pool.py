import pylru
from hashlib import sha256 as H256
from transactions import SignedTransaction
from enum import Enum

class Strategy(Enum):
    FIFO = 1
    PRIORITY = 2
    VIP = 3

class Filter:
    fields = [
        ('key', H256),
        ('value', int)
    ]

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = pylru.lrucache(self.capacity)

    def check(self, key):
        return key in self.cache

class TxOrder:
    fields = [
        ('hash', H256),
        ('order', long)
    ]

    def __init__(self, hash, order):
        self.hash = hash
        self.order = order

    def Eq(self):
        pass

    def ParitalEq(self):
        pass

    def Ord(self):
        pass

class Pool(Filter):
    
    fields = [
        ('package_limit', int),
        ('filter', Filter),
        ('order_set', int),
        ('txs', SignedTransaction),
        ('strategy', Strategy),
        ('order', long)
    ]

    def __init__(self, package_limit, filter, order_set, txs, strategy, order):
        self.package_limit = package_limit
        pass

def main():
    filter = Filter(capacity=100)
    print filter.check(1)
    pool = Pool(100, filter, 1, 1, 1, 1)
    print "It's Ok!"
    pass

if __name__ == "__main__":
    main()
