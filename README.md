# hioki_ohmmeter
Unofficial ROS driver of hioki ohmmeter (currently using RM3545)

# usage
```
 # to print data to standard output
 rosrun hioki_ohmmeter print.py <serial port>
 # to publish data to ROS network
 rosrun hioki_ohmmeter publish.py <serial port>
```
# udev file setup if needed (E.g. /dev/ohmmeter)
```
rosrun hioki_ohmmeter ohmmeter_udev_setup.sh              
```


# Official USB driver and Manual (in Japanese)
https://www.hioki.co.jp/jp/support/versionup/detail/?downloadid=1094

# Sample communication program w/o ROS (in Japanese)
https://www.hioki.co.jp/jp/support/versionup/detail/?downloadid=1384

# Reference as ROS driver of sensor/transducer
https://github.com/sktometometo/imada_forcegauge.git
