# MAKE THE PICO RUN THIS CODE 

import machine
import time

button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

print("Pico macro engine started...")

while True:
    if button.value() == 0:
        print("TRIGGER_MACRO")
        time.sleep(2) 
    time.sleep(0.05)
