#!/bin/sh

echo "#udev id for ohmmeter
SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"108f\", ATTRS{idProduct}==\"0001\", SYMLINK+=\"ohmmeter\"" > /tmp/72-ohmmeter-udev.rules

sudo sh -c "cat /tmp/72-ohmmeter-udev.rules > /etc/udev/rules.d/72-ohmmeter-udev.rules"

sudo udevadm control --reload-rules
sudo adduser $USER dialout

echo ""
echo "ohmmeter udev setup has finished."

