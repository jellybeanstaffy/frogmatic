##frogmatic v1.0.0
##component code 1
from tkinter import *
from time import sleep
from tkinter import messagebox
import urllib.request
from random import randint
import frank
#from bibblebobble import speechbubble

def setup():
    frank.appear(1,100,100)
    frank.setsprite('searchingwifi.gif')
    try:
        urllib.request.urlopen('https://github.com')
    except:
        print('err:nowifi')
        frank.setsprite('nowifi.gif')
        messagebox.showerror('oops...','unable to connect')
        frank.disappear(1)
        exit()
    frank.appear(3,100,100)
    frank.gomono()
    try:
        r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/update.py')
        with open('install.dat','wb')as w:
            w.write(r.read())
            w.close()
        sleep(1)
        with open('install.dat','r')as r:
                exec(r.read())
                r.close()
        #print('updater temporarily disabled to prevent changes from self destructing :)')
    except:
        print('err:update failed')
        messagebox.showerror('frogmatic update','an error occured whilst updating the program')
        try:
            urllib.request.urlopen('https://github.com')
        except:
            print('err: connection lost')
            frank.disappear(3)
            frank.setsprite('nowifi.gif')
            messagebox.showerror('oops...','unable to connect')
            frank.disappear(1)
    frank.gounmono()
    frank.bubble.say('experimental speech',5)


    #sleep(5)



    #exit()
def run():
    setup()
    while True: 
        try:
            tmp = input("?}>")
            exec(tmp)
        except Exception as e:
            print('err:'+str(e))

