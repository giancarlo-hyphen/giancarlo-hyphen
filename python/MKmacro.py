# -------------------------------------------------------------------#
# Script for starting  a .exe file and saving the output to a logfile#
#--------------------------------------------------------------------#

#Mouse and Keyboard Automation Python

import pyautogui 
#import pandas as pd   
#import datetime

#pyautogui.moveRel(9,0, duration=1) #If you want to move mouse again relative to position

#Click with mouse
pyautogui.moveTo(110, 10)
pyautogui.click(button='right', clicks=1)
pyautogui.moveRel(20, 145)
pyautogui.moveRel(145, 0, duration=1)
pyautogui.moveRel(0, 74, duration=0.5)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')


