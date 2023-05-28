#V: Laku_2023_05_08
import sys
import subprocess


packages = ['pywin32', 'keyboard', 'ctypes', 'pillow', 'pyautogui', 'pyperclip']

def install(package1):
    try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package1])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package1}: {str(e)}")




package=packages[0]
try:
    import win32api
    print( package + 'alredy installed')
except:
    install(package)
    
input('next')

package=packages[1]
try:
    import keyboard
    print( package + 'alredy installed')
except:
    install(package)
    
input('next')
    
package=packages[2]
try:
    import ctypes
    print( package + 'alredy installed')
except:
    install(package)
    
input('next')

package=packages[3]
try:
    import PIL
    print( package + 'alredy installed')
except:
    install(package)
    
input('next')

package=packages[4]
try:
    import pyautogui
    print( package + 'alredy installed')
except:
    install(package)
    
input('next')

package=packages[5]
try:
    import pyperclip
    print( package + 'alredy installed')
except:
    install(package)
    
input('finish')


