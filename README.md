# hackster.io-2015
Made for the hackster.io hackathon at the Kickstarter headquaters in Brooklyn, NY.
Team members:
 Gabe Chai
 Samson Fung
 Zoilo Mercedes
 Michael Sy
 Kevin Yan
 
Setup:
  Edison:
    Connect buttons on pins 2, 4, 6, 8 and 10.
    Connect the controls for the relay to pin 13
    Connect LED LCD Grove display to the I2C port on the Grove Base Shield
  Arduino Uno:
    Connect the temperature probe into pin 2
    The probe's model number is DS18B
  Connect the tx and rx pins on the Arduino Uno and the Edison.

Usage:
  Run main.py on the edison
  Compile and upload DS18x20_Temperature.ino inside the Arduino_Uno folder with when PIN 0 is unplugged
    After upload, plug in pin 0
  Follow directions on the LED LCD display.
