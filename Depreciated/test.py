#!/usr/bin/env python  
  
import mraa  
import time  

pin = raw_input("What pin #?\n")
pin = int(pin)  
led = mraa.Gpio(pin)  
led.dir(mraa.DIR_IN)  
  
while True:  
    print led.read()
    time.sleep(.3)
 


