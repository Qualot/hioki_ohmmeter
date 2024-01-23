#! /usr/bin/env python3
# coding: utf-8

import serial
import time
import sys

from ohmmeter import OhmMeter

if __name__=="__main__":

    if len( sys.argv ) < 2:
        print("print ohmmeter data")
        print("usage:program <serial port> <print rate (optional default: 10Hz)>")
        sys.exit(1)

    a = OhmMeter( sys.argv[1] )
    if len( sys.argv ) > 2:
        try:
            rate = int(sys.argv[2])
        except:
            rate = 10
    else:
        rate = 10
    dt = 1.0 / rate

    try:
        while True:
            print( str(a.read()) )
            time.sleep(dt)
    except KeyboardInterrupt:
        del a
