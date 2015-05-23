import mraa
import sys
import time
import socket
import fcntl
import struct

buttonPin = 13

buttonState = 0

while 1:
	buttonState = buttonPin.read():
	print buttonState