'''
By Abdullah Siddiqui

Script to be used on a computer
This script takes the temperature from the micro:bit that is running
Midway_Reciever.py and gives an alert on your phone it to your phone
'''

import serial
import time
import requests
import sys

# the port used to connect your computer to the micro:bit

# for linux
if sys.platform.lower() == 'linux' or 'linux2':
    port = "/dev/ttyACM0"

# for Windows
elif sys.platform.lower() == 'win32':
    port = "COM0"
    
# for Mac
elif sys.platform.lower() == 'darwin':
    pass

# the connection speed needed to for the micro:bit and the computer to communicate
baud = 115200

# configures the serial port and the speed of the connection
s = serial.Serial(port)
s.baudrate = baud

def send_alarm_to_phone(location, fahrenheit, celcius):
    report = {}
    report["value1"] = f"{location} is on fire and the temperature is {fahrenheit}°F or {celcius}°C"
    requests.post("https://maker.ifttt.com/trigger/Fire/with/key/IFTTT Code", params=report)
    
while True:
    data = s.readline().decode("utf-8")[:-2].split(':')
    location = data[0]
    data_celcius = data[1]
    data_fahrenheit = data[2]
    
    send_alarm_to_phone(location, data_fahrenheit, data_celcius)
    
    time.sleep(1)
