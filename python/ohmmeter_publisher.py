#! /usr/bin/env python
# coding: utf-8

import rospy
from hioki_ohmmeter.msg import OhmMeterData
from ohmmeter import OhmMeter
import time
import sys

class OhmMeterPublisher:
    """
    The class to publish the output of HIOKI RM3545 
    """

    def __init__( self, topicname, serialport, baudrate = 115200, timeout = 0.01, nodename = "OhmMeter"):
        """
        Constructor

        引数
            topicname: topic name to be published
            serialport: the path to device file of RM3545 (e.g. "/dev/ttyACM0")
            baudrate: baudrate of serial communication (default: 119200)
            timeout: timeout of serial communication (default: 0.01 s)
            nodename: node's name (Default: OhmMeter)
        """
        self.ohmmeter = OhmMeter( serialport, baudrate=baudrate, timeout=timeout)

        rospy.init_node( nodename )
        self.publisher = rospy.Publisher( topicname, OhmMeterData, queue_size=10 )

    def __del__( self):
        """
        """
        #self.ohmmeter.__del__()
        del self.ohmmeter

    def publish(self, timeout):
        """
        publish
        """
        publishdata = OhmMeterData()
        publishdata.data = float(self.ohmmeter.read(timeout))
        publishdata.header.stamp = rospy.Time.now()
        self.publisher.publish(publishdata)
