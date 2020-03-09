'''
By Abdullah Siddiqui

Script to be flashed on a micro:bit that is connected to a computer
This script takes the temperature from the radio that is sent form the fire estinguisher and then prints it out
'''

from microbit import *
import radio

# Turns on the radio
radio.on()
radio.config(channel=15)

# defines a function named celsuis_to_fahrenheit which takes in a location and a temperature
def celsuis_to_fahrenheit(location, celsuis_temp):
    # Converts the celsuis temperature
    fahrenheit_temp = (int(celsuis_temp) * 9/5) + 32
    
    # Prints out the location, the celsuis temperature, and the fahrenheit temperature to be used with the serial module in your computer to recieve data and send notification to your phone
    print('{}:{}:{}'.format(location, str(celsuis_temp), str(int(fahrenheit_temp))))
    
    # Scrolls out the location, the celsuis temperature, and the fahrenheit temperature to the display
    display.scroll('{}:{}:{}'.format(location, str(celsuis_temp), str(int(fahrenheit_temp))))

# Runs the loop for ever
while True:
    message = radio.receive()
    
    # Checks to see is there are any new messages
    if message is not None:
        temp = message.split(':')[0]
        device_location = message.split(':')[1]
        
        celsuis_to_fahrenheit(device_location, temp)
    
    else:
        pass
    
    sleep(100)

# Turns the radio off
radio.off()