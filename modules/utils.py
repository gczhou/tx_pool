try:
    from Crypto.Hash import keccak
    sha3_256 = lambda x: keccak.new(digest_bits=256, data=x).digest()
except:
    import sha3 as _sha3
    sha3_256 = lambda x: _sha3.keccak_256(x).digest()

import rlp
from rlp.utils import decode_hex, encode_hex as _encode_hex, ascii_chr, str_to_bytes

is_numeric = lambda x: isinstance(x, int)

def sha3(seed):
    sha3_count[0] += 1
    return sha3_256(to_bytes(seed))

def int_to_addr(x):
    o = [b''] * 20
    for i in range(20):
        o[19 - i] = ascii_chr(x & 0xff)
        x >>= 8
    return b''.join(o)

def normalize_address(x, allow_blank=False):
    if is_numeric(x):
        return int_to_addr(x)
    if allow_blank and x in {'', b''}:
        return b''
    if len(x) in (42, 50) and x[:2] in {'0x', b'0x'}:
        x = x[2:]
    if len(x) in (40, 48):
        x = decode_hex(x)
    if len(x) == 24:
        assert len(x) == 24 and sha3(x[:20])[:4] == x[-4:]
        x = x[:20]
    if len(x) != 20:
        raise Exception("Invalid address format: %r" % x)
    return x

def main():
    normalize_address("ea4f6bc98b456ef085da5c424db710489848cab5")
    print "It's OK!"

if __name__ == "__main__":
    main()