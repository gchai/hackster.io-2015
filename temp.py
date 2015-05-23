#!/usr/bin/env python  
  
import mraa
import sys
import time

tempio = mraa.Aio(0)   

while 1:
	tempread = tempio.read()
    tempres = float(1023-tempread)*10000/tempread

    tempC = 1/(log(tempres/10000)/3975+1/298.15)-273.15
    print tempC
    time.sleep(.2)