import tx_pool

class CandidatePool:
    fields = [
        ('pool', tx_pool),
        ('height', int),
        ('sender', long)
    ]

    def __init__(self):
        self.pool = tx_pool::pool(1000)
        self.height = 0
        self.sender = Sender

    def get_height(self):
        return self.height

    def meet_conditions(self, height):
        return self.height == height

    def broadcast_tx(self, tx):
        pass

    def add_tx(self, unverified_tx, is_from_broadcast):
        pass

    def spawn_new_block(self, height, hash):
        pass

    def pub_block(self, block):
        pass

    def update_txpool(self, txs[]):
        pass