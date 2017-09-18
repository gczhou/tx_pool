import pylru
from hashlib import sha256 as H256

FIFO = 0
PRIORITY = 1
VIP = 2

class Filter:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = pylru.lrucache(self.capacity)

    def check(self, key):
        return key in self.cache   

class Pool:
    def __init__(self, package_limit, ):
        self.package_limit = package_limit,
        self.filter = Filter
#        filter: Filter,
#    order_set: BTreeSet<TxOrder>,
#    txs: HashMap<H256, SignedTransaction>,
#    strategy: Strategy,
#    order: u64,

def main():
    filter = Filter(capacity=100)
    print filter.check(1)
    pass

if __name__ == "__main__":
    main()
        
