#V: Laku_2023_05_08
try:
    import keyboard
    from pyautogui import *
    import win32api, win32con
    import time
    import pyperclip as pc
    import os
    import sys
    import win32gui
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    print('One or more modules not found')
    input()
    exit()
Ppath = os.path.join(os.getcwd().replace("\\Import", ""), "Data/StringImportingMousePositions")
try:
    open(Ppath)
except:
    print('No Mouse position file found')
    input()
    exit()
with open(Ppath) as posse:
    poss=posse.readlines()
    
    her= poss[0].split('.')
    x1 = (int(her[0].split(',')[0]),int(her[0].split(',')[1]))
    x2 = (int(her[1].split(',')[0]),int(her[1].split(',')[1]))

#CHANGE THESE TWO VARIABLES VVV
mousePositionForCopying = x1
mousePositionForDone = x2
#CHANGE THESE TWO VARIABLES ^^^





Path = os.path.join(os.getcwd().replace("\\Import", ""), "Data/strings")







def main():
    userIn='i'
    if(userIn == 'i'):
        try:
            strings = open(Path,"r")
        except:
            print("No text file named 'strings' was found.")
            input()
            exit()

    
    print("Strings file found.")
    segments = strings.readlines()
    print("String segments obtained, " + str(len(segments)) + " were found.")
    delay = 0.5
    input("\nPress enter to ready up the string import process. It will start when your active window is Rec room. Before that ensure that the following are true: \n\nYou are seated in the importing seat.  \nYou are holding makerpen in you left hand with the 'connect' tool selected. \nYou are holding the trigger handle in you right hand. \nYou are looking straight at the first list input")
    insert(segments,delay)

def insert(list,delay):
    while True:
        handle = win32gui.GetForegroundWindow()
        if win32gui.GetWindowText(handle) == 'Rec Room':
            break
    win32api.SetCursorPos((0,0))
    (x,y) = mousePositionForCopying
    (x2,y2) = mousePositionForDone
    for i in enumerate(list):
        if keyboard.is_pressed('q'):
            exit()
        
        (index,string) = i
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        if keyboard.is_pressed('p'):
            sleep(5)
            while True:
                if keyboard.is_pressed('p'):
                    break
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            exit()
        
        win32api.SetCursorPos((x,y))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        pc.copy(string)
        time.sleep(delay)
        hotkey('ctrl','v')
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            exit()
        
        win32api.SetCursorPos((x2,y2))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        


main()
