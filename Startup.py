import vlc
import time
import os

vid = vlc.MediaPlayer('video.mp4')

def playvid():
    vid.play()
    print('i did it')
    time.sleep(1)
    vid.set_fullscreen(True)
    ms = vid.get_length()
    sec = ms / 1000
    time.sleep(sec)
    print(f'{sec} seconds')

while True:
    if 'explorer.exe' in os.popen('tasklist').read().lower():
        playvid()
        break
    else:
        break