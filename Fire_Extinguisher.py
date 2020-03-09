'''
By Abdullah Siddiqui

Script to be used on the fire estinguisher
This script takes the temperature from the thermometer and based on that sends the tempreture by sends a radio message.
The it turns on the speaker, the lights, and the water pump
'''

from microbit import *
import radio
import music

try:
    # Turns on the radio
    radio.on()
    radio.config(channel=15)

# The location of the fire sprinkler
device_location = 'Guest Room'
while True:
    # Gets the temperature and stores it in the variable called temp
    temp = temperature()
    
    # Checks if the variable temp is greater then or equal to 57°C
    if temp >= 57:
        # Turns on the water pump
        pin0.write_digital(1)
        # Sends a radio message with the temp and device_location variable
        radio.message('{}:{}'.format(str(temp), device_location))
        
    sleep(1000)
    
# Turns off the radio
radio.off()

________________________________________________________________________________________________________________
# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
radio.config(channel=15)

def image(seconds):
    display.show(Image("90000"*5))
    sleep(seconds)
    display.show(Image("09000"*5))
    sleep(seconds)
    display.show(Image("00900"*5))
    sleep(seconds)
    display.show(Image("00090"*5))
    sleep(seconds)
    display.show(Image("00009"*5))
    sleep(seconds)

    
device_location = 'Guest Room'
while True:
    
    if pin0.read_analog() >= 135:
        radio.message('{}:{}'.format(str(int(pin0.read_analog())), device_location))
        pin1.write_digital(1)
        pin2.write_digital(1)
        image(100)
        sleep(20000)
    
    
    sleep(1000)
    
radio.off()

__________________________________________
from microbit import *

while True:
    display.show(Image("99000:"*5))
    sleep(300)
    display.show(Image("00099:"*5))
    sleep(300)
    
________________________________________________
# Write your code here :-)
from microbit import *
import audio


def read_frame(f_list, frame):
    for file in f_list:
        ln = file.readinto(frame)
        while ln:
            yield frame
            ln = file.readinto(frame)


def play_file(f):
    with open(f, "rb") as file1
        f_list = [file1]
        audio.play(read_frame(f_list, frame), wait=True)


# Allocate memory outside the interrupt
frame = audio.AudioFrame()
ln = -1
file = 1
# play the files
play_file("output.raw")


__________________________________________________
from microbit import *
import radio
import music

radio.on()
radio.config(channel=15)

def image():
    for i in range(10):        
        display.show(Image("99000:"*5))
        sleep(300)
        display.show(Image("00099:"*5))
        sleep(300)
    
def play_alarm():
    for i in range(10):
        music.play('b5:5',pin=pin1)
        sleep(15)  

    
device_location = 'Guest Room'
while True:
    
    if int(((pin0.read_analog() * (3000 / 1023.0) - 100.0) / 10) - 40) >= 22:
        radio.send('{}:{}'.format(str(int(((pin0.read_analog() * (3000 / 1023.0) - 100.0) / 10) - 40)), device_location))
        pin2.write_digital(1)
        image()
        play_alarm()
        sleep(2000)
        pin2.write_digital(0)
        display.clear()
    
    else:
        pass
    sleep(1000)
    
radio.off()
