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
print('move cursor to the string input field')
while True:
    if keyboard.is_pressed('q'):
        pos1=win32api.GetCursorPos()
        break
pos1 = str(pos1).replace('(','')
pos1 = str(pos1).replace(')','')
print(pos1)
sleep(1)
print('move cursor to the outside of makerpen UI')
while True:
    if keyboard.is_pressed('q'):
        pos2=win32api.GetCursorPos()
        break
pos2 = str(pos2).replace('(','')
pos2 = str(pos2).replace(')','')
print(pos2)
with open('StringImportingMousePositions','a') as file:
    pass
with open('StringImportingMousePositions','w') as file:
    pass
with open('StringImportingMousePositions','a') as file:
    file.write(f'{pos1}.{pos2}')
