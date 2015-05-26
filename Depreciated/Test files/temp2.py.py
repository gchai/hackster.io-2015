#!/usr/bin/env python  
  
import mraa
import sys
import time
import socket
import fcntl
import struct
import math

import pyupm_12clcd as lcd

tempio = mraa.Aio(0)
# Initialize Jhd1313m1 @ 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)   
myLCD = lcd.Jhd1313ml(0, 0x3E, 0x62)


while 1:
	tempread = tempio.read()
    tempres = float(1023-tempread) * 10000/tempread
    tempC = 1/(match.log(tempres/10000)/39.75 + 1/298.15) - 273.15
    tempF = tempC*9/5 + 32

    print "TempC: %f, TempF: %f" % (tempC, tempF)
    
    myLCD.clear()
    myLCD.setColor(255,255,0)
    myLCD.setCursor(0,0)
    tempString = string(tempC) + " " + string(tempF)
    myLCD.write(tempString)
    time.sleep(.2)