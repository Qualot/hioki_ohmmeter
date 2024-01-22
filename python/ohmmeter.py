#! /usr/bin/env python
# coding: utf-8

"""
Ohmmeter driver class
"""

import serial
import time
import sys

class OhmMeter(object):
    """
    Class of RM3545
    """

    def __init__( self, serialport, baudrate = 119200, timeout = 0.01):
        """
        Constructor

        arguments
            serialport : path to serial device (E.g. "/dev/ttyACM0")
            baudrate   : baudrate (bps)
            timeout    : timeout (sec)
        """
        self.serialport = serialport
        self.baudrate = baudrate
        self.serdev = serial.Serial( serialport, baudrate = baudrate, timeout = timeout)

    def __del__( self ):
        """
        Constructor
        """
        self.serdev.close()

    def read(self):
        """
        read the output of the ohmmeter
        """
        self.serdev.write(b"D\r")
        string = self.serdev.read(10)
        try:
            return float(string[:-4])
        except ValueError:
            return 0

