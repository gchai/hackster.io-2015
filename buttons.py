import mraa
import sys
import time
import socket
import fcntl
import struct

var buttonPin = 13

var buttonState = 0

while 1:
	buttonState = buttonPin.read():
	print buttonState