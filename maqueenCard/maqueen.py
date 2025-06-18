# MIT License
#
# Copyright (c) 2021 Kristoffer Holm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import microbit
import neopixel
import utime

class Maqueen:
    """
    A class to control the DFRobot Maqueen robot with the BBC micro:bit.

    Supports motor control (I2C 0x10), LED control, RGB LEDs, line sensors,
    ultrasonic distance measurement, and servo motors.
    """

    def __init__(self):
        """Initialises Maqueen, including NeoPixel LEDs."""
        self.neo = neopixel.NeoPixel(microbit.pin15, 4)
        microbit.pin1.write_digital(0)  # Setup ultrasonic trigger pin

    def led_left(self, value):
        """
        Controls the left LED.
        
        :param value: 1 to turn ON, 0 to turn OFF.
        """
        microbit.pin8.write_digital(value)

    def led_right(self, value):
        """
        Controls the right LED.
        
        :param value: 1 to turn ON, 0 to turn OFF.
        """
        microbit.pin12.write_digital(value)

    def rgb_front_left(self, red, green, blue):
        """
        Sets the front left RGB LED color.

        :param red: Red component (0-255)
        :param green: Green component (0-255)
        :param blue: Blue component (0-255)
        """
        self.neo[0] = (red, green, blue)
        self.neo.show()

    def rgb_rear_left(self, red, green, blue):
        """
        Sets the rear left RGB LED color.
        """
        self.neo[1] = (red, green, blue)
        self.neo.show()

    def rgb_rear_right(self, red, green, blue):
        """
        Sets the rear right RGB LED color.
        """
        self.neo[2] = (red, green, blue)
        self.neo.show()

    def rgb_front_right(self, red, green, blue):
        """
        Sets the front right RGB LED color.
        """
        self.neo[3] = (red, green, blue)
        self.neo.show()

    def motor_left(self, speed):
        """
        Controls the left motor via I2C.

        :param speed: -255 (full reverse) to 255 (full forward)
        """
        data = bytearray(3)
        data[0] = 0x00  # Left motor ID
        data[1] = 1 if speed < 0 else 0  # 1 = reverse, 0 = forward
        data[2] = abs(speed)  # Speed value (0-255)
        microbit.i2c.write(0x10, data)

    def motor_right(self, speed):
        """
        Controls the right motor via I2C.

        :param speed: -255 (full reverse) to 255 (full forward)
        """
        data = bytearray(3)
        data[0] = 0x02  # Right motor ID
        data[1] = 1 if speed < 0 else 0  # 1 = reverse, 0 = forward
        data[2] = abs(speed)  # Speed value (0-255)
        microbit.i2c.write(0x10, data)

    def line_left(self):
        """
        Checks if the left line sensor detects a line.

        :return: 1 if line detected, 0 otherwise.
        """
        return microbit.pin13.read_digital()

    def line_right(self):
        """
        Checks if the right line sensor detects a line.

        :return: 1 if line detected, 0 otherwise.
        """
        return microbit.pin14.read_digital()

    def servo_one(self, angle=0):
        """
        Moves servo 1 to a specific angle.

        :param angle: Angle in degrees (0-180)
        """
        data = bytearray(2)
        data[0] = 0x14
        data[1] = angle
        microbit.i2c.write(0x10, data)

    def servo_two(self, angle=0):
        """
        Moves servo 2 to a specific angle.

        :param angle: Angle in degrees (0-180)
        """
        data = bytearray(2)
        data[0] = 0x15
        data[1] = angle
        microbit.i2c.write(0x10, data)

    def ultrasound_measure(self):
        """
        Measures distance using the ultrasonic sensor.

        :return: Distance in centimeters, or -1/-2 on failure.
        """
        microbit.pin1.write_digital(1)
        utime.sleep_us(10)
        microbit.pin1.write_digital(0)

        # Wait for echo
        timeout = utime.ticks_us()
        while True:
            pulseBegin = utime.ticks_us()
            if microbit.pin2.read_digital():
                break
            if (pulseBegin - timeout) > 5000:
                return -1  # Timeout

        # Measure echo duration
        while True:
            pulseEnd = utime.ticks_us()
            if not microbit.pin2.read_digital():
                break
            if (pulseEnd - pulseBegin) > 5000:
                return -2  # Timeout

        pulse_time = pulseEnd - pulseBegin
        return int(pulse_time / 58)  # Convert to cm

