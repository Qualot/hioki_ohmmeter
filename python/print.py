#! /usr/bin/env python3
# coding: utf-8

import sys
import time
from absl import app
from absl import flags

from ohmmeter import OhmMeter

Timeout_default = 1

FLAGS = flags.FLAGS
flags.DEFINE_string("serial_port", "/dev/ohmmeter0", "Serial port: (default) /dev/ohmmeter0")
flags.DEFINE_integer("print_rate", 10, "Print rate in Hz: (default) 10")

def main(argv):
    if FLAGS.serial_port is None:
        print("Serial port not provided. Usage: program --serial_port=<serial port> [--print_rate=<print rate>]")
        sys.exit(1)

    a = OhmMeter(FLAGS.serial_port)
    rate = FLAGS.print_rate
    dt = 1.0 / rate

    a.start_measure()

    try:
        while True:
            print(float(a.read(Timeout_default)))
            time.sleep(dt)
    except KeyboardInterrupt:
        a.stop_measure()
        del a

if __name__ == "__main__":
    app.run(main)
