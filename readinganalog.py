#!/usr/bin/env python  
  
import mraa
import sys

pot = mraa.Aio(0)   

while 1:
    potVal = float(pot.read())
    print potVal