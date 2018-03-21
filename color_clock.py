# Transition times for RED: (Up) [21-0] <> (Down) [9-12]
# Transition times for GREEN: (Up) [12-15, 21-0] <> (Down) [3-6, 18-21]
# Transition times for BLUE: (Up) [6-9, 21-0] <> (Down) [0-3, 15-18]
# 42.3529411765

import datetime
import threading
import Tkinter
from Tkinter import *

window = Tk()
    



app = 0
now = 0
hour = 0
minimum = 0
maximum = 255
time = 60*(60/(float(maximum-minimum)/3))
rgb = [maximum,maximum,maximum]
transitionColor = 2
transitionType = False
label = Label(window, text="", fg="white")

def start():
    now = datetime.datetime.now()
    global hour
    hour = now.hour
    changeIncrement(backThree(hour))
    setValuesInit(backThree(hour))
    global time
    pastEighth = int(round(float(timeInSeconds()) / time))
    if transitionColor != 3:
        if transitionType:
            rgb[transitionColor] += pastEighth
        else:
            rgb[transitionColor] -= pastEighth
    else:
        rgb[0] += pastEighth
        rgb[1] += pastEighth
        rgb[2] += pastEighth
    printout = "(" + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + ")"
    label.configure(text=printout)
    label.pack()

def refreshTime():
    global time
    threading.Timer(time, refreshTime).start()
    now = datetime.datetime.now()
    hour = now.hour
    bgcolor = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
    window.configure(background=bgcolor)
    if transitionColor != 3:
        rgb[transitionColor] = increment(rgb[transitionColor])
    else:
        incrementAll()
    if reachedExtreme():
        changeIncrement(checkHour(hour))
    printRGB(rgb[0], rgb[1], rgb [2])

def timeInSeconds():
    now = datetime.datetime.now()
    second = now.second
    minute = now.minute * 60
    hour = (now.hour % 3) * 3600
    return second + minute + hour

def printRGB(r,g,b):
    printout = "(" + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + ")"
    label.configure(text=printout)
    label.config(bg="black")
    label.pack()

def increment(color):
    if transitionType:
        return color + 1
    else:
        return color - 1

def incrementAll():
    rgb[0] += 1
    rgb[1] += 1
    rgb[2] += 1
    
def reachedExtreme():
    if (transitionColor != 3):
        if (rgb[transitionColor] == minimum or rgb[transitionColor] == maximum):
            return True
        else:
            return False
    else:
        if rgb[0] == maximum:
            return True
        
def changeIncrement(timeHour):
    global transitionColor
    global transitionType
    # Decreasing green
    if timeHour == 3 or timeHour == 18:
        transitionColor = 1
        transitionType = False
    # Increasing blue
    elif timeHour == 6:
        transitionColor = 2
        transitionType = True
    # Decreasing red
    elif timeHour == 9:
        transitionColor = 0
        transitionType = False
    # Increasing green
    elif timeHour == 12:
        transitionColor = 1
        transitionType = True
    # Decreasing blue
    elif timeHour == 15 or timeHour == 0:
        transitionColor = 2
        transitionType = False
    # Increasing red, green, and blue
    elif timeHour == 21:
        transitionColor = 3
        transitionType = True

def setValuesInit(currentHour):
    global maximum
    global minimum
    if currentHour == 0:
        rgb[0] = maximum
        rgb[1] = maximum
        rgb[2] = maximum
    elif currentHour == 3:
        rgb[0] = maximum
        rgb[1] = maximum
        rgb[2] = minimum
    elif currentHour == 6:
        rgb[0] = maximum
        rgb[1] = minimum
        rgb[2] = minimum
    elif currentHour == 9:
        rgb[0] = maximum
        rgb[1] = minimum
        rgb[2] = maximum
    elif currentHour == 12:
        rgb[0] = minimum
        rgb[1] = minimum
        rgb[2] = maximum
    elif currentHour == 15:
        rgb[0] = minimum
        rgb[1] = maximum
        rgb[2] = maximum
    elif currentHour == 18:
        rgb[0] = minimum
        rgb[1] = maximum
        rgb[2] = minimum
    elif currentHour == 21:
        rgb[0] = minimum
        rgb[1] = minimum
        rgb[2] = minimum

def checkHour(inHour):
	if inHour == 23:
		return 0
	if inHour % 3 == 2:
		return inHour + 1
	else:
		return inHour
	
def backThree(currentHour):
    return currentHour - (currentHour % 3)
    
window.title('Color Clock')
window.geometry("400x400")
#app.attributes('-fullscreen', True)
start()
refreshTime()
window.mainloop()
