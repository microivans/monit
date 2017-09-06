#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket

def test_port():

    # IP address from command line:
    address = sys.argv[1]
    # Port from command line:
    ports = [25, 80, 8080, 8999] 
   
    print ("The following ports will be scanned:")
    print (ports) 
    for port in ports: 
        s = socket.socket()
        try:
            s.connect((address, port))
        # Refused
        except ConnectionRefusedError:
            print ("Port %s is inaccessible" % port)
        # Success
        else:
            print ("Port %s is accessible" % port)
            s.close()  
    

if __name__ == "__main__":
    test_port()
