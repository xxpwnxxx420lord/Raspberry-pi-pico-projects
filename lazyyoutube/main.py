# run this in vsc / real python

import serial
import time
import pyautogui

pyautogui.PAUSE = 0.1 

port = "COM3"
baud_rate = 115200

print("Listening for Pico button press...")
ser = serial.Serial(port, baud_rate, timeout=1)

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line == "TRIGGER_MACRO":
            print("🚀 Button pressed! Starting automation...")
            
            pyautogui.press('win')
            time.sleep(0.5)
            
            pyautogui.write('chrome')
            pyautogui.press('enter')
            
            time.sleep(2)
            
            pyautogui.hotkey('ctrl', 't')
            time.sleep(0.5)
            
            pyautogui.write('youtube.com')
            pyautogui.press('enter')
            time.sleep(4) 
            
            pyautogui.click(2013, 594)
            print("Clicked at coordinates.")
            
            print("Waiting 7 seconds...")
            time.sleep(7)
            
            pyautogui.press('f')
            print("Automation complete!")
            
    except Exception as e:
        pass
    time.sleep(0.05)
