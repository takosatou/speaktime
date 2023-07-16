#! /usr/bin/python3

# If you use PWM with Raspberry Pi Zero,
# add /boot/config.txt the following line
#   dtoverlay=audremap,pins_12_13
# then reboot it

import subprocess as sp
import datetime

def speaktime(t):
    h = t.hour
    m = t.minute
    
    if h >= 13:
        h -= 12
    m10 = (m // 10) * 10
    m1 = m % 10

    # 00 1ji
    # 01 1ji 1m
    # 10 1ji 10m
    # 11 1ji 10 1m
    
    files = [f'{h}ji.wav']
    if m != 0:
        if m1 == 0:
            files.append(f'{m10}m.wav')
        elif m10 == 0:
            files.append(f'{m1}m.wav')
        else:
            files.append(f'{m10}.wav')
            files.append(f'{m1}m.wav')

    # print(files)
    for f in files:
        sp.run(['/usr/bin/aplay', '-q', f])


def test_speaktime():
    for m in range(60):
      h = m % 13
      t = datetime.datetime(year=2023, month=7, day=1,
                            hour=h, minute=m, second=0)
      speaktime(t)
 

if __name__ == '__main__':
    t = datetime.datetime.now()
    speaktime(t)
    # test_speaktime()    
    
