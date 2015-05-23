import mraa
import sys
import time
import socket
import fcntl
import struct

buttonState = 0
buttonPin = 13

while 1:
	buttonState = buttonPin.read()
	print buttonState