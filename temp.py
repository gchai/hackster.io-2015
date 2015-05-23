#!/usr/bin/env python  
  
import mraa
import sys

pot = mraa.Aio(0)   

while 1:
    potVal = float(pot.read())
    temp = ((potVal*5.0/1024.0)-0.5) * 100
    print(temp)

