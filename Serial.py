# http://www.keithedavey.ca/2015/02/19/light-blue-python/
"""Serial.py: read available data from LightBlue-Bean's serial port via BLE"""
import sys
if not '/usr/local/lib/python2.7/site-packages' in sys.path:
	# print '/usr/local/lib/python2.7/site-packages not in the path, adding...'
	sys.path.append('/usr/local/lib/python2.7/site-packages')
	# print '{}\n'.format(sys.path)

import serial # pip install pyserial
from serial import tools
from time import sleep

#check ports available with: python -m serial.tools.list_ports'

# SERIAL_PORT = '/dev/cu.LightBlue-Bean'	#<-bean loader says this is the path and it works on Arduino IDE.
# SERIAL_PORT = '/dev/tty.LightBlue-Bean'	#
# SERIAL_PORT = '/tmp/tty.LightBlue-Bean'	#
# SERIAL_PORT = '/tmp/cu.LightBlue-Bean'	#<- 1st path is a symlink to this one
SERIAL_PORT = '/dev/cu.Bluetooth-Incoming-Port' # <-- this is the only port found by script in line 12
BAUD_RATE = 57600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
# ser = serial.Serial('dev/ttys004')
# ser.open()
ser.write(b'hello';
print 'Starting reading from: {}'.format(ser.name)

while True:
	if ser.inWaiting() > 0:
		data = ser.read(inWaiting())
		print 'data received: {}'.format(data)