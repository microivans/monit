#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket

def test_port():
    s = socket.socket()
    # IP address from command line:
    address = sys.argv[1]
    # Port from command line:
    port = int(sys.argv[2])
    try:
        s.connect((address, port))
    # Refused
    except ConnectionRefusedError:
        sys.exit(1)
    # Success
    else:
        s.close()
        sys.exit(0)

if __name__ == "__main__":
    test_port()
