#!/usr/bin/env python  
  
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


while 1:
    tempread = tempio.read()
    tempres = float(1023-tempread) * 10000/tempread
    tempC = 1/(math.log(tempres/10000)/3975 + 1/298.15) - 273.15
    tempF = tempC*9/5 + 32

    print "TempC: %f, TempF: %f" % (tempC, tempF)
    
    myLCD.clear()
    myLCD.setColor(255,255,0)
    myLCD.setCursor(0,0)


    myLCD.write(str(tempC))
    myLCD.setCursor(1,0)
    myLCD.write(str(tempF))
    time.sleep(.2)