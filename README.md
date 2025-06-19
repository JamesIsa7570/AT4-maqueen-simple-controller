# AT4-maqueen-simple-controller
For the AT4 assessment. This repository contains the code and documentation for a simple radio controlled maqueen.

## How I built this Maqueen controller.


I first read up on what hardware components the Maqueen is made up of. Sources include: https://wiki.dfrobot.com/SKU_MBT0021-EN_Maqueen_Plus_STEAM_Programming_Educational_Robot https://www.manualslib.com/manual/2630665/Dfrobot-Mbt0021-En.html https://introduction-to-robotics-using-maqueen.readthedocs.io/en/latest/tutorials/maqueen-programming-python.html#led-light-flash


After I had done that I decided what way I was going to talk to the Maqueen from my computer. I decided I’d use it’s radio over it’s Bluetooth, due to my time and knowledge constraints.


Then I went and looked for the Maqueen API so I would know what functions are connected to the radio. I found https://python.microbit.org/v/3. This website has a references page and an API page, both of which I used.


From there I sent button presses ‘A’ & ‘B’ from the microbit connected to the computer, to the other microbit in the Maqueen. I made it move forward (‘A’) and right (‘B’) as a proof of concept and test if the radio code was working.


Once I got it working I made a simple keyboard input in Thonny and built up simple ‘if’ statements in the Maqueens’ microbit. After some more testing I got my finished product.


Based on the other licenses used (such as the Maqueen license being MIT), this repositories’ licence will be MIT (as per the licensing question from AT4 assessment).
