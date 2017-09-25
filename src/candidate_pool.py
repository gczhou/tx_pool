from .tx_pool import Pool
from proto.lib import *
from proto.blockchain_pb2 import *

class CandidatePool:
    fields = [
        ('pool', Pool),
        ('height', int)
    ]

    def __init__(self, tx):
        self.pool = Pool(10000)
        self.height = 0
        self.sender = tx

    def get_height(self):
        return self.height

    def meet_conditions(self, height):
        return self.height == height

    def broadcast_tx(self, tx):
        msg = create_msg(submodules.CONSENSUS, topics.NET_TX, MsgType.TX, tx.SerializeToString())
        print("braodcast new tx")
        self.sender.put(msg)

    def add_tx(self, unverified_tx, is_from_broadcast):
        content = TxResponse()
        trans = verify_transaction(unverified_tx)

        pass

    def spawn_new_block(self, height, hash):
        pass

    def pub_block(self, block):
        pass

    def update_txpool(self, txs):
        pass