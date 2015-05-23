#!/usr/bin/env python  
  
import mraa
import sys
import time

tempio = mraa.Aio(0)   

while 1:
    print float(tempio.read())
    time.sleep(.2)
