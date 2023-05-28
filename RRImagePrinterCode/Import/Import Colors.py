#V: Laku_2023_05_08
try:
    import win32gui
    from pyautogui import *
    import win32api, win32con
    import time
    import pyperclip as pc
    import keyboard
    import os
    import sys
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    print('one or more modules missing')
    input()
    exit()
Path = os.path.join(os.getcwd().replace("\\Import", ""), "Data/CustomColors")
Ppath = os.path.join(os.getcwd().replace("\\Import", ""), "Data/ColorImportingMousePositions")
try:
    open(Ppath)
except:
    print('no mouse position file found')
    input()
    exit()
with open(Ppath) as posse:
    poss=posse.readlines()
    
    her= poss[0].split('.')
    x1 = (int(her[0].split(',')[0]),int(her[0].split(',')[1]))
    x2 = (int(her[1].split(',')[0]),int(her[1].split(',')[1]))
    x3 = (int(her[2].split(',')[0]),int(her[2].split(',')[1]))
    x4 = (int(her[3].split(',')[0]),int(her[3].split(',')[1]))


mousePositionForcolor = x1
mousePositionForcustom = x2
mousePositionFortext = x3
mousePositionForoutside = x4

#This variable controls what button you use to open makerpen palette
button= 'f'
#This variable controls what button you use to open makerpen palette



def main():
    userIn='i'
    if(userIn == 'i'):
        try:
            with open(Path,"r")as file:
                strings=file.readlines()

        except:
            print("No text file named 'CustomColors' was found.")
            input()
            exit()

    
    print("Custom colors file found.")
    delay = 0.5
    input("\nPress enter to ready up the process\nMake sure you have the trigger handle in right hand and a makerpen on the left with the recoloring tool.\nAlso make sure your cotrol setting are so u can open makerpen palette with the letter 'F'.\n look straight at the pen that is point toward the print area so the one thats pointing at you (not the floor)")
    
    insert(strings, delay)
def insert(list,delay):
    while True:
        handle = win32gui.GetForegroundWindow()
        if win32gui.GetWindowText(handle) == 'Rec Room':
            break
    win32api.SetCursorPos((0,0))
    (x,y) = mousePositionForcolor
    (x2,y2) = mousePositionForcustom
    (x3,y3) = mousePositionFortext
    (x4,y4) = mousePositionForoutside
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(delay)

    for i in (list):
        
        heax=(i.split('.'))[2].strip()
        
        
        if keyboard.is_pressed('q'):
            exit()
        
        keyboard.press(button)
        keyboard.release(button)
        if keyboard.is_pressed('p'):
            sleep(5)
            while True:
                if keyboard.is_pressed('p'):
                    break
        time.sleep(delay)
        
        win32api.SetCursorPos((x,y))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        if keyboard.is_pressed('p'):
            sleep(5)
            while True:
                if keyboard.is_pressed('p'):
                    break
        time.sleep(delay)
        win32api.SetCursorPos((x2,y2))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            exit()
        if keyboard.is_pressed('p'):
            sleep(5)
            while True:
                if keyboard.is_pressed('p'):
                    break
        win32api.SetCursorPos((x3,y3))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        pc.copy(heax)
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            exit()
        
        hotkey('ctrl','v')
        time.sleep(delay)
        
        win32api.SetCursorPos((x4,y4))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        if keyboard.is_pressed('q'):
            exit()
        
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(delay)
        


main()
