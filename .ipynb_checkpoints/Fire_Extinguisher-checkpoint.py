'''
By Abdullah Siddiqui

Script to be used on the fire estinguisher
This script takes the temperature from the thermometer and based on that sends the tempreture by sends a radio message.
The it turns on the speaker, the lights, and the water pump
'''

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
