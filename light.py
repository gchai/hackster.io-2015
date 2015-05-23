#!/usr/bin/env python  

import mraa
from flask import Flask
app = Flask(__name__)

lightPin = mraa.Aio(1)

@app.route("/light")
def light():
    return str(lightPin.read())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
