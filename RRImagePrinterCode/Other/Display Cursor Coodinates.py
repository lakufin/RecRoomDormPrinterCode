#V: Laku_2023_05_08
try:
    import ctypes
    import time
    import win32api
    import ctypes
except:
    print('one or more module missing')
    input()
    exit()
user32 = ctypes.windll.user32 
user32.SetProcessDPIAware()

while True:
    time.sleep(1)
    print(win32api.GetCursorPos())