import pyautogui
import time
import os
import pyscreeze
import sys

__author__ = "Sahal Mulki"

global mode
mode = sys.argv[1]

print("Made by Sahal Mulki")
print("     H     ")
print("     A     ")
print("     C     ")
print("     K     ")
print("     E     ")
print("     R     ")
print("           ")
print("     C     ")
print("     L     ")
print("     I     ")
print("     C     ")
print("     K     ")
print("     E     ")
print("     R     ")
 
if mode == "cookie":

    input1 = input("Would you Like to (I)nfinity Tap or Tap the cookie a (S)pecified amount of times")
    
    if input1 == "I": 


        screen = pyscreeze.screenshot()
        cookie = pyscreeze.locateOnScreen('cookie.png')
        try:
            screen = pyscreeze.screenshot()
            cookie = pyscreeze.locateOnScreen('cookie.png')
            cookiex, cookiey = pyscreeze.center(cookie)
        except TypeError:
            helo = input("Cookie not found :(")
            os._exit(0)

        pyautogui.moveTo(cookiex, cookiey)

        i = 0
        while True:
            pyautogui.click()
            time.sleep(0.0005)
            i += 1
            print(i)
    elif input1 == "S" :
        input3 = int(input("Enter number of times cookie will be clicked"))
        
        screen = pyscreeze.screenshot()
        cookie = pyscreeze.locateOnScreen('cookie.png')
        cookiex, cookiey = pyscreeze.center(cookie)

        pyautogui.moveTo(cookiex, cookiey)
        
        while input3 != 0:
            try:
                pyautogui.click()
                input3 -= 1
                time.sleep(0.0005)
                print(input3)
            except:
                print("Error")
                
        if input3 == 0:
            print("DONE!")
            time.sleep(10)

elif mode == "doge":

    input6 = input("How many cycles do you want to execute?")
    input7 = input("Put your cursor on rock")
    
    i = 0
    for x in range(int(input6)):
        for x in range(100):
            
            pyautogui.click()
            time.sleep(0.0005)
            i += 1
            print(i)
        print("Collect your coins")
        time.sleep(3)
    
    
