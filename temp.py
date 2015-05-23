#!/usr/bin/env python  
  
import mraa
import sys
import time

tempio = mraa.Aio(0)   

while 1:
    tempres = float(1023-tempio * 10000/tempio)
    tempC = 1/log(tempres/10000)/3975+1/298.15)-273.15
	time.sleep(.2)
	print tempC