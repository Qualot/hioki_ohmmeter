#! /usr/bin/env python3
# coding: utf-8

import rospy
from ohmmeter_publisher import OhmMeterPublisher
import sys
from absl import app
from absl import flags

Timeout_default = 1

FLAGS = flags.FLAGS
flags.DEFINE_string("serial_port", "/dev/ohmmeter0", "Serial port")
flags.DEFINE_string("output_topic", "OhmMeter", "Output topic")

def main(argv):
    if FLAGS.serial_port is None:
        print("Serial port not provided. Usage: program --serial_port=<serial port> [--output_topic=<output topic>]")
        sys.exit(1)

    print(f"Serial port: {FLAGS.serial_port}")
    print(f"Output topic: {FLAGS.output_topic}")

    a = OhmMeterPublisher(FLAGS.output_topic, FLAGS.serial_port)
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

if __name__ == "__main__":
    app.run(main)
