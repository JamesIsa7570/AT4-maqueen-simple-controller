from microbit import *
from maqueen import Maqueen
import radio
import os
import music

radio.on()
radio.config(group=25)
maqueen = Maqueen()

maqueen.led_left(1)
maqueen.led_right(1)
lights = "on"

set_volume(100)

while True:
    message = radio.receive()
    
    if message == "w":
        # forward
        maqueen.motor_left(150)
        maqueen.motor_right(150)
        sleep(1000)
        maqueen.motor_left(0)
        maqueen.motor_right(0)
    if message == "a":
        # left
        maqueen.motor_left(-150)
        maqueen.motor_right(150)
        sleep(100)
        maqueen.motor_left(0)
        maqueen.motor_right(0)
    if message == "s":
        # back
        maqueen.motor_left(-150)
        maqueen.motor_right(-150)
        sleep(500)
        maqueen.motor_left(0)
        maqueen.motor_right(0)
    if message == "d":
        # right
        maqueen.motor_left(150)
        maqueen.motor_right(-150)
        sleep(100)
        maqueen.motor_left(0)
        maqueen.motor_right(0)
        
    if message == "e":
        if lights == "on":
            maqueen.led_left(0)
            maqueen.led_right(0)
            lights = "off"
        else:
            maqueen.led_left(1)
            maqueen.led_right(1)
            lights = "on"

    if message == "q":
        music.play(music.BA_DING)

    if message == "z":
        maqueen.motor_left(255)
        maqueen.motor_right(255)
        sleep(1500)
        maqueen.motor_left(0)
        maqueen.motor_right(0)
