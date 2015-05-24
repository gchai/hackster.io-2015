import mraa
import sys
import time
import socket
import fcntl
import struct

tempUpPin = 2 
tempDownPin = 4
timeUpPin = 6
timeDownPin = 8

	tempUp = mraa.Gpio(tempUpPin)
	tempUp.dir(mraa.DIR_IN)

	tempDown = mraa.Gpio(tempDownPin)
	tempDown.dir(mraa.DIR_IN)

	timeUp = mraa.Gpio(timeUpPin)
	timeUp.dir(mraa.DIR_IN)

	timeDown = mraa.Gpio(timeDownPin)
	timeDown.dir(mraa.DIR_IN)

while 1:
	time.sleep(.5)

	print "Temperature Up: %d, Temperature Down: %d" % (tempUp.read(), tempDown.read())
	print "Time Up: %d, Time Down: %d" % (timeUp.read(), timeDown.read())