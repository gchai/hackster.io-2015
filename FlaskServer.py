#!/usr/bin/env python  

import mraa
import sys
from flask import Flask
app = Flask(__name__)

lightPin = mraa.Aio(1)
tempPin=mraa.Aio(0)
soundPin = mraa.Aio(2)

@app.route("/pebble")
def pebble():
	tempVal = float(tempPin.read())
	temp = ((tempVal*5.0/1024.0)-0.5) * 100
	lightVal = 1024-lightPin.read()
	sound = soundPin.read()
	pebbleinfo = "{"+"temp"+":"+str(temp)+","+"light"+":"+str(lightVal)+","+"sound"+":"+str(sound)+"}"
	return pebbleinfo


if __name__ == "__main__":
    app.run(host='0.0.0.0')