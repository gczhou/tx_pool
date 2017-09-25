import pylru
from enum import Enum

from transactions import SignedTransaction

class Strategy(Enum):
    FIFO = 1
    PRIORITY = 2
    VIP = 3

class Filter:
    fields = [
        ('key', long),
        ('value', int)
    ]

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = pylru.lrucache(self.capacity)

    def check(self, key):
        return key in self.cache

class TxOrder:
    fields = [
        ('hash', long),
        ('order', long)
    ]

    def __init__(self, hash, order):
        self.hash = hash
        self.order = order

    def Eq(self):
        pass

    def ParitalEq(self, other):
        return self == other

    def PartialOrd(self, other):
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

    def __init__(self, package_limit, capacity):
        self.package_limit = package_limit
        self.filter = Filter(capacity)
        self.order_set = None
        self.txs = None
        self.strategy = Strategy.FIFO
        self.order = 0

    def get_order():
        pass

    def get_order_by_priority():
        pass

    def get_order_by_vip():
        pass

    def enqueue(tx):
        pass

    def update_order_set():
        pass

    def update(txs):
        pass

    def package(height):
        pass