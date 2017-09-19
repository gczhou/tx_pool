# -*- coding: utf-8 -*-

import time
import gipc

from modules import start_pubsub

def main():
    print "In main process"
    (tx, rx) = gipc.pipe(duplex=True)
    pass

if __name__ == "__main__":
    main()