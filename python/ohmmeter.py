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

    def start_measure(self):
        """
        start the free-run mode
        """
        self.sendMsg((":INIT:CONT ON"))

    def stop_measure(self):
        """
        start the free-run mode
        """
        self.sendMsg((":INIT:CONT OFF"))

    def read(self, timeout):
        """
        read the output of the ohmmeter
        """
        #self.serdev.write(b"D:FETCh?\r\n")
        #string = self.serdev.read(10)
        string = self.SendQueryMsg(":FETCh?", timeout)
        try:
            return float(string)
        except ValueError:
            return 1e+30

    #Command sending
    def sendMsg(self, strMsg):
        ret = False

        try:
            strMsg = strMsg + '\r\n'                #Adding terminator CR+LF
            self.serdev.write(bytes(strMsg, 'utf-8'))  #Sending by converting to Byte type
            ret = True
        except Exception as e:
            print("Send Error")
            print(e)

        return ret
    
    #Command receiving
    def receiveMsg(self, timeout):

        msgBuf = bytes(range(0))                    #received data

        try:
            start = time.time()                     #time record for timeout calculation
            while True:
                if self.serdev.inWaiting() > 0:        #data in buffer?
                    rcv = self.serdev.read(1)          #receive 1 byte
                    if rcv == b"\n":                #end when receiving terminator LF
                        msgBuf = msgBuf.decode('utf-8')
                        break
                    elif rcv == b"\r":              #neglect terminator CR
                        pass
                    else:
                        msgBuf = msgBuf + rcv
                
                #timeout processing
                if  time.time() - start > timeout:
                    msgBuf = "Timeout Error"
                    break
        except Exception as e:
            print("Receive Error")
            print(e)
            msgBuf = "Error"

        return msgBuf
    
    #Command send/receive
    def SendQueryMsg(self, strMsg, timeout):
        ret = self.sendMsg(strMsg)
        if ret:
            msgBuf_str = self.receiveMsg(timeout)   #If send is OK, to receive
        else:
            msgBuf_str = "Error"

        return msgBuf_str