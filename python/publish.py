#! /usr/bin/env python3
# coding: utf-8

import rospy
from ohmmeter_publisher import OhmMeterPublisher
import time
import sys

Timeout_default = 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("publish force data read from imada forcegauge")
        print("usage:program <serial port> <output topic (optional, default:ForceGauge)>")
        sys.exit(0)

    if len(sys.argv) > 2:
        topicname = sys.argv[2]
    else:
        topicname = "ForceGauge"

    a = OhmMeterPublisher(topicname, sys.argv[1])
    a.ohmmeter.start_measure()

    try:
        r = rospy.Rate(10)  # 10Hz
        while not rospy.is_shutdown():
            a.publish(Timeout_default)
            r.sleep()

    except KeyboardInterrupt:
        a.ohmmeter.stop_measure()
        del a
        sys.exit(0)
