#pip install python-vlc
import  vlc
import time

def playPattern(pn):
    p = vlc.MediaPlayer("./Patterns/" + str(pn) +".mp3")
    p.play()
    print(str(pn))
    time.sleep(8)
    p.stop()