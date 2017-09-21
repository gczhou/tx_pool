# -*- coding: utf-8 -*-

import time
import gipc
import threading

from threadpool import *

from src.start_pubsub import start_pubsub
from src.candidate_pool import *
from src.dispatch import *

THREAD_POOL_NUMBER = 2

def key_to_id():
    pass

def parse_msg():
    pass

def dealMsgBody(body, tx):
    (cmd_id, origin, content) = parse_msg(body)
    tx.put(key_to_id(key), cmd_id, origin, content)

def recMsgFun(tx, rx, threadpool):
    while True:
        (key, body) = rx.get()
        requests = makeRequests(dealMsgBody, (body, tx), None)
        [threadpool.putRequest(req) for req in requests]
        threadpool.wait()

def main():
    print("Tx_pool main process starts!!!")
    (tx_sub, rx_sub) = gipc.pipe(duplex=True)
    (tx_pub, rx_pub) = gipc.pipe(duplex=True)
    (tx, rx) = gipc.pipe(duplex=True)
    keys = ["net.*", "consensus_cmd.default", "consensus.blk", "chain.status", "jsonrpc.new_tx"]
    pool = ThreadPool(THREAD_POOL_NUMBER)
    start_pubsub("consensus", keys, tx_sub, rx_pub)

    #接收MQ模块发来的信息
    threading.Thread(target=recMsgFun, args=(tx, rx_sub, pool))
    
    #发送信息
    candidate_pool = CandidatePool(tx_pub)
    while True:
        pass

if __name__ == "__main__":
    main()
