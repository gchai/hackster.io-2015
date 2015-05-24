import mraa

tempPin = 13

tempSensor = mraa.Gpio(tempPin)
tempSensor.dir(mraa.DIR_IN)

while 1:
	print tempSensor.read()
