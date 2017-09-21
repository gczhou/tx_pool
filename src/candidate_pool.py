from .tx_pool import Pool

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
        pass

    def add_tx(self, unverified_tx, is_from_broadcast):
        pass

    def spawn_new_block(self, height, hash):
        pass

    def pub_block(self, block):
        pass

    def update_txpool(self, txs):
        pass