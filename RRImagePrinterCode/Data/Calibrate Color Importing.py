#V: Laku_2023_05_08
try:
    import keyboard
    import win32api
    from time import sleep
    import ctypes
    import os
    import sys
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    print('one or more module missing')
    input()
    exit()
user32 = ctypes.windll.user32 
user32.SetProcessDPIAware()

print('ready to calibrate, press q to capture coordinates')
print('Open makerpen palette and choose recolor tool.')
print('move cursor to the color button')
while True:
    if keyboard.is_pressed('q'):
        pos1=win32api.GetCursorPos()
        break
pos1 = str(pos1).replace('(','')
pos1 = str(pos1).replace(')','')
print(pos1)
sleep(1)
print('press the color button and move cursor to the custom button')
while True:
    if keyboard.is_pressed('q'):
        pos2=win32api.GetCursorPos()
        break
pos2 = str(pos2).replace('(','')
pos2 = str(pos2).replace(')','')
print(pos2)

sleep(1)
print('move cursor to the hex color input field')
while True:
    if keyboard.is_pressed('q'):
        pos3=win32api.GetCursorPos()
        break
pos3 = str(pos3).replace('(','')
pos3 = str(pos3).replace(')','')
print(pos3)


print('move cursor to the outside of makerpen UI')
sleep(1)
while True:
    if keyboard.is_pressed('q'):
        pos4=win32api.GetCursorPos()
        break
pos4 = str(pos4).replace('(','')
pos4 = str(pos4).replace(')','')
print(pos4)


with open('ColorImportingMousePositions','a') as file:
    pass
with open('ColorImportingMousePositions','w') as file:
    pass
with open('ColorImportingMousePositions','a') as file:
    file.write(f'{pos1}.{pos2}.{pos3}.{pos4}')
