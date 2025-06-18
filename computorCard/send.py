from microbit import *
import radio

radio.config(group=25)
radio.on()

while True:
    keyboard = input('Input: ')
    radio.send(keyboard)
