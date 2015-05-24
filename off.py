import mraa


inputpin = 13


alwaysOn = mraa.Gpio(inputpin)
alwaysOn.dir(mraa.DIR_OUT)
while 1:
	alwaysOn.write(0)