
#----------------------------Mouse and Keyboard Automation Python------------------------------------------#
# Move the mouse and click on the first file at the coordinates 37,133 ( it just under the recycle bin) ---#
#--------------Then it will paste the clipboard to that file and save + exit-------------------------------#
#---------------------------------Author: Giancarlo Hernandez Ponce----------------------------------------#
#----------------------------------------------------------------------------------------------------------#

import pyautogui 
import os

#Variables
#cmd = "TASKKILL /F /IM notepad.exe" 


#pyautogui.moveRel(0,1, duration=1) #If you want to move mouse again relative to position

#Click with mouse # skip the movement
pyautogui.doubleClick(37, 133)
pyautogui.click(194,850)
pyautogui.click(194,850)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 's')

pyautogui.displayMousePosition()

#Executes a system command that closes notepad
os.system(cmd)

