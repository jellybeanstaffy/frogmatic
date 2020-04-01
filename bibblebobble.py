##bibblebobble v0.0.1
##component code 1
from tkinter import *
def speechbubble(speech):
    global frogmatic,canvas,img
    try:
        Label(frogmatic, speech, column=0,row=0)
    except Exception as e:
        print(e)
        
