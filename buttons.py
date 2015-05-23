import mraa
import sys
import time
import socket
import fcntl
import struct

buttonState = 0
buttonPin = 13

while 1:
	button = mraa.Gpio(buttonPin)
	buttonState = button.read()
	print buttonState
	time.sleep(.2)