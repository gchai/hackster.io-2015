import mraa
import sys
import time
import socket
import fcntl
import struct

temperature = 100
time = 10

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

def TempChange(tempUp, tempDown):
	if tempUp == 1:
		temperature += 1
	elif tempDown == 1:
		temperature -= 1
	return temperature

def TimeChange(timeUp, timeDown):
	if timeUp == 1:
		time += 10
	elif timeDown == 1:
		time -= 10
	return time

while 1:
	time.sleep(.5)
	
	print TempChange()
	print TimeChange()

	print "Temperature Up: %d, Temperature Down: %d" % (tempUp.read(), tempDown.read())
	print "Time Up: %d, Time Down: %d" % (timeUp.read(), timeDown.read())
