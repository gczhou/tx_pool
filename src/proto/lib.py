from enum import Enum

class submoudules(Enum):
    JSON_RPC = 1
    NET = 2
    CHAIN = 3
    CONSENSUS = 4
    CONSENSUS_CMD = 5
    AUTH = 6

class topics(Enum):
    DEFAULT = 0
    REQUEST = 1
    NEW_BLK = 2
    NEW_STATUS = 3
    SYNC_BLK = 4
    RESPONSE = 5
    NEW_TX = 6
    TX_RESPONSE = 7
    CONSENSUS_MSG = 8
    NEW_PROPOSAL = 9
    VERIFY_TX_REQ = 10
    VERIFY_TX_RESP = 11
    VERIFY_BLK_REQ = 12
    VERIFY_BLK_RESP = 13
    BLOCK_TXHASHES = 14
    BLOCK_TXHASHES_REQ = 15

def topic_to_string(top):
    if top == topics.DEFAULT:
        return "default"
    elif top == topics.REQUEST:
        return "request"
    elif top == topics.NEW_BLK:
        return "new_blk"
    elif top == topics.NEW_STATUS:
        return "new_status"
    elif top == topics.SYNC_BLK:
        return "sync_blk"
    elif top == topics.RESPONSE:
        return "tx_response"
    elif top == topics.NEW_TX:
        return "new_tx"
    elif top == topics.TX_RESPONSE:
        return "tx_response"
    elif top == topics.CONSENSUS_MSG:
        return "consensus_msg"
    elif top == topics.NEW_PROPOSAL:
        return "new_proposal"
    elif top == topics.VERIFY_TX_REQ:
        return "verify_tx_req"
    elif top == topics.VERIFY_TX_RESP:
        return "verify_tx_resp"
    elif top == topics.VERIFY_BLK_REQ:
        return "verify_blk_req"
    elif top == topics.VERIFY_BLK_RESP:
        return "verify_blk_resp"
    elif top == topics.BLOCK_TXHASHES:
        return "block_txhashes"
    elif top == topics.BLOCK_TXHASHES_REQ:
        return "block_txhashes_req"
    else:
        return ""

def id_to_key(id):
    if id == submodules.JSON_RPC: 
        return "json_rpc"
    elif id == submodules.NET:
        return "net"
    elif id == submodules::CHAIN:
        return "chain"
    elif id == submodules::CONSENSUS:
        return "consensus"
    elif id == submodules::CONSENSUS_CMD:
        return "consensus_cmd"
    elif id == submodules::AUTH:
        return "auth"
    else:
        return ""

def key_to_id(key):
    if key.starts_with("jsonrpc"):
        return submodules.JSON_RPC
    elif key.starts_with("net"):
        return submodules.NET
    elif key.starts_with("chain"):
        return submodules::CHAIN
    elif key.starts_with("consensus_cmd"):
        return submodules::CONSENSUS_CMD
    elif key.starts_with("consensus"):
        return submodules::CONSENSUS
    elif key.starts_with("auth"):
        return submodules::AUTH
    else:
        return 0

def create_msg(sub, top, msg_type, content):
    pass

def 

