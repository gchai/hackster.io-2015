import mraa
import sys
import time
import socket
import fcntl
import struct
import math

import pyupm_i2clcd as lcd

tempio = mraa.Aio(0)
# Initialize Jhd1313m1 @ 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)   
myLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

temperature = 100
clocktime = 10

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
	global temperature
	if temperature >= 80:
		if tempUp == 1:
			temperature += 1
		if not(temperature == 80):
			if tempDown == 1:
				temperature -= 1
	return temperature

def TimeChange(timeUp, timeDown):
	global clocktime
	if clocktime >= 0:
		if timeUp == 1:
			clocktime += 10
		if not(clocktime == 0):
			if timeDown == 1:
				clocktime -= 10
	return clocktime










while 1:
	time.sleep(.5)
	
	tempread = tempio.read()
	tempres = float(1023-tempread) * 10000/tempread
 	tempC = 1/(math.log(tempres/10000)/3975 + 1/298.15) - 273.15
	tempF = tempC*9/5 + 32
	
	myLCD.clear()
	myLCD.setColor(255,255,0)
	myLCD.setCursor(0,0)
	myLCD.write(str(tempF))

	myLCD.setCursor(1,0)
	bottomDisplay = str(TempChange(tempUp.read(), tempDown.read())) +  " " + str(TimeChange(timeUp.read(), timeDown.read()))

	myLCD.write(bottomDisplay)



	print "Temperature Up: %d, Temperature Down: %d" % (tempUp.read(), tempDown.read())
	print "Time Up: %d, Time Down: %d" % (timeUp.read(), timeDown.read())


