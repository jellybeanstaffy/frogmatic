##frogmatic v1.0.0
##component code 1
from tkinter import *
from time import sleep
from tkinter import messagebox
import urllib.request
global frogmatic,canvas,img
from random import randint
#from bibblebobble import speechbubble
def gonuts():##BAD BEHAVIOUR
    global frogmatic,canvas,img
    for x in range(1,25):
        print('err:bibblebobble component error#'+str(randint(1,10)))
        img = PhotoImage(file='da_'+str(randint(0,50))+'.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        frogmatic.update()
        position(randint(0,100),randint(0,100))
    frogmatic.destroy()

    messagebox.showerror('critical error','critical error')
    with open('database.dat','w')as w:
        w.write('ERRORCODE RUNTIME ATTEMPT REINSTALLATION')
        w.close()
    exit()
















def disappear(dtype):
    global frogmatic,canvas,img
    if dtype==1:#dissapearance type one: from black frog to exit
        for x in range(26,51):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
        exit()
    if dtype==2:#dessapearance type two: from colourfull frog to exit
        for x in range(0,51):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
        exit()
    if dtype==3:#dessapearance type two: from colourfull frog to black frog
        for x in range(0,27):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
def position(xpos,ypos):
    global frogmatic,canvas,img
    frogmatic.update_idletasks()
    width = frogmatic.winfo_width()
    height = frogmatic.winfo_height()
    x = ((frogmatic.winfo_screenwidth() // 100)*xpos) - (width // 2)
    y = ((frogmatic.winfo_screenheight() // 100)*ypos) - (height // 2)
    frogmatic.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    canvas.create_image(0,0, anchor=NW, image=img)
    frogmatic.update()
def gomono():
    global frogmatic,canvas,img
    for x in range(20,120,20):
        img = PhotoImage(file='mono@'+str(x)+'%.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        sleep(0.1)
        frogmatic.update()
def gounmono():
    global frogmatic,canvas,img
    for x in range(100,0,-20):
        img = PhotoImage(file='mono@'+str(x)+'%.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        sleep(0.1)
        frogmatic.update()
def setup():
    global frogmatic,canvas,img
    try:
        frogmatic.destroy()
    except:
        pass
    frogmatic=Tk()
    frogmatic.attributes("-topmost", True)
    frogmatic.geometry('384x216')
    frogmatic.title('frogmatic')
    frogmatic.iconbitmap('frog.ico')
    frogmatic.configure(bg='#fff')
    frogmatic.overrideredirect(True)
    frogmatic.wm_attributes("-transparentcolor",'#fff')
    canvas = Canvas(frogmatic, width = 384, height = 216,highlightthickness=0)      
    canvas.grid(row=0,column=0,columnspan=5,rowspan=5)
    img = PhotoImage(file='da_50.gif')
    position(90,90)
    for x in range(50,25,-1):
        img = PhotoImage(file='da_'+str(x)+'.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        frogmatic.update()
    img = PhotoImage(file='searchingwifi.gif')
    canvas.create_image(0,0, anchor=NW, image=img)
    frogmatic.update()

    try:
        urllib.request.urlopen('https://github.com')
    except:
        print('err:nowifi')
        img = PhotoImage(file='nowifi.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        frogmatic.update()
        messagebox.showerror('oops...','unable to connect')
        disappear(1)
    for x in range(25,-1,-1):
        img = PhotoImage(file='da_'+str(x)+'.gif')
        canvas.create_image(0,0, anchor=NW, image=img)        
        frogmatic.update()
    gomono()
    try:
        r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/update.py')
        with open('install.dat','wb')as w:
            w.write(r.read())
            w.close()
        sleep(1)
        with open('install.dat','r')as r:
                exec(r.read())
        print('updater temporarily disabled to prevent changes from self destructing :)')
    except:
        print('err:update failed')
        messagebox.showerror('frogmatic update','an error occured whilst updateing the program')
        try:
            urllib.request.urlopen('https://github.com')
        except:
            print('err: connection lost')
            disappear(3)
            img = PhotoImage(file='nowifi.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
            messagebox.showerror('oops...','unable to connect')
            disappear(1)
    gounmono()
    gonuts()##BAD BEHAVIOUR



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

