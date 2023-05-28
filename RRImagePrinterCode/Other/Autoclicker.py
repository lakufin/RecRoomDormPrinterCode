#V: Laku_2023_05_08
try:
    import win32con
    import win32api
    import keyboard
    from time import sleep
    
except:
    print('one or more module missing')
    input()
    exit()
sleep(5)
while True:
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    sleep(4)
    if keyboard.is_pressed('q'):
        exit()