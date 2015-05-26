import mraa
import sys
import time
import socket
import fcntl
import struct

buttonState = 0
buttonPin = 2

while 1:
	time.sleep(.5)
	button = mraa.Gpio(buttonPin)
	button.dir(mraa.DIR_IN)
	buttonState = button.read()
	print buttonState