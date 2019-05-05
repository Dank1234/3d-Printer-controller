import requests
import keyboard
x = "20"
y = "20"
z = "20"
e = "0"



requests.get('http://192.168.137.203/set?code=G28%27)
requests.get('http://192.168.137.203/set?code=G0 Z20 X20 Y20')
while True:
    if keyboard.is_pressed('a'):
        x = int(x)
        x = x-1
        x = str(x)
    if keyboard.is_pressed('d'):
        x = int(x)
        x = x+1
        x = str(x)
    if keyboard.is_pressed('s'):
        y = int(y)
        y = y-1
        y = str(y)
    if keyboard.is_pressed('w'):
        y = int(y)
        y = y+1
        y = str(y)
    if keyboard.is_pressed('q'):
        z = int(z)
        z = z-1
        z = str(z)
    if keyboard.is_pressed('e'):
        z = int(z)
        z = z+1
        z = str(z)
    if keyboard.is_pressed('z'):
        e = int(e)
        e = e+1
        e = str(e)
    if keyboard.is_pressed('x'):
        e = int(e)
        e = e-1
        e = str(e)
    if keyboard.is_pressed('c'):
        requests.get('http://192.168.137.203/set?code=G28%27)
        print('Homing...')
    if keyboard.is_pressed('p'):
        requests.get('http://192.168.137.203/set?code=M112%27)
        print('STOPPING!')
        print('reboot printer to resume use')
        exit()

    requests.get('http://192.168.137.203/set?code=' + 'G0 Y' + y + 'X' + x + 'Z' + z + 'E' + e)