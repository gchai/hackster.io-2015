# Sous Vide Machine w/ Arduino Controls
# For Hackster.io 2015
# May 24, 2015
# Samson Fung, Gabriel Chai, Michael Sy, Zoilo Mercedes, Kevin Yan

import mraa
import time
import math

import pyupm_i2clcd as lcd

tempio = mraa.Aio(0)
# Initialize Jhd1313m1 @ 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)   
myLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

startButtonPin = 2
tempUpPin = 4
tempDownPin = 6
timeUpPin = 8
timeDownPin = 10

potPin = 13

# Code is for Fahrenheit temperatures
def TempChange(temperature, tempUp, tempDown):
	if temperature >= 80:
		if tempUp.read() == 1:
			temperature += 1
		if not(temperature == 80):
			if tempDown.read() == 1:
				temperature -= 1
	return temperature

def TimeChange(timer, timeUp, timeDown):
	if timer >= 0:
		if timeUp.read() == 1:
			timer += 60
		if not(timer == 0):
			if timeDown.read() == 1:
				timer -= 60
	return timer

# For Analog Reader
def temperature():
	tempread = tempio.read()

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

	return (tempC, tempF)

def display(line1, line2):
	myLCD.clear()
	myLCD.setColor(255,255,0)
	myLCD.setCursor(0,0)
	myLCD.write(str(line1))

	myLCD.setCursor(1,0)
	myLCD.write(str(line2))

def main():
	tempUp = mraa.Gpio(tempUpPin)
	tempUp.dir(mraa.DIR_IN)

	tempDown = mraa.Gpio(tempDownPin)
	tempDown.dir(mraa.DIR_IN)

	timeUp = mraa.Gpio(timeUpPin)
	timeUp.dir(mraa.DIR_IN)

	timeDown = mraa.Gpio(timeDownPin)
	timeDown.dir(mraa.DIR_IN)

	startButton = mraa.Gpio(startButtonPin)
	startButton.dir(mraa.DIR_IN)

	pot = mraa.Gpio(potPin)
	pot.dir(mraa.DIR_OUT)

	initTemp = 100
	initTime = 600

	start = False

	while start == False:
		initTemp = TempChange(initTemp, tempUp, tempDown)
		initTime = TimeChange(initTime, timeUp, timeDown)

		line1 = str(initTemp) + " degrees F."
		line2 = str(initTime/60) + " minutes"
		display(line1, line2)
		if startButton.read() == 1:
			start = True

	print "START"
	
	# startTime = time.time()
	# pot.write(1)

	# while time.time() - startTime <= initTime:


	# pot.write(0)


main()