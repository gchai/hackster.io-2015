import socket
import fcntl
import struct

import pyupm_i2clcd as lcd

def get_ip_address(ifname):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# Clear
myLcd.clear()

# Green
myLcd.setColor(0, 255, 255)
x=1
r=1
g=1
b=1
while True:
	myLcd.setCursor(0,0)
#	ip_address = get_ip_address('wlan0')
	myLcd.write('Hello World! %d' % (x))
	x+=1
	myLcd.setColor(r%255,g%255,b%255)
	r+=2
	g+=1
	b+=3
