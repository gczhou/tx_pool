import rlp
from enum import Enum

import utils

class Action(Enum):
    Store = 1
    Create = 2
    Call = 3

class Transaction(rlp.Serializable):
    fields = [
        ('nonce', int),
        ('gas_price', int),
        ('gas', int),
        ('action', Action),
        ('value', int),
        ('data', long),
        ('block_limit', int)
    ]

    _sender = None
    _hash = None

    def __init__(self, nonce, gas_price, gas, value, data, block_limit):
        super(Transaction, self).__init__(nonce, gas_price, gas, value, data, block_limit)
        # log.debug('deserialized tx', tx=encode_hex(self.hash)[:8])

    def decodable(self):
        pass

    def encodable(self):
        pass

    def nonce(self):
        return self.nonce

    def action(self):
        return self.action

class UnverifiedTransaction(Transaction):
    fields = [
        ('unsigned_transaction', Transaction),
        ('signature', int),
        #TODP
        #('crypto_type', CryptoType),
        ('hash', long)
    ]
    
    def __init__(self):
        pass

    def deref(self):
        pass

    def decodable(self):
        pass

    def encodable(self):
        pass

class SignedTransaction:
    fields = [
        ('transaction', UnverifiedTransaction),
        #('sender', Address),
        #('public', Public)
    ]

    def __init__(self):
        pass
    
    def decodable(self):
        pass

    def encodeable(self):
        pass
