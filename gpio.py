import mraa


inputpin = 13


alwaysOn = timemraa.Gpio(inputpin)
alwaysOn.dir(mraa.DIR_OUT)
while 1:
	alwaysOn = 1