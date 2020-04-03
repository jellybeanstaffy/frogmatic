##frank v0.5.2
##component code 1
from tkinter import *
from time import sleep
from tkinter import messagebox
global frogmatic,canvas,img
#from bibblebobble import speechbubble
def appear(atype,posx,posy):#ap[earance types
    global frogmatic,canvas,img
    if atype==1 or atype==2:
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
        position(posx,posy)
    if atype==1:#none to black
        for x in range(50,25,-1):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
    if atype==2:
        for x in range(50,-1,-1):#non to colour 
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
    if atype==3:#black to colour
        for x in range(26,-1,-1):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
def disappear(dtype):#disappearance types
    global frogmatic,canvas,img
    if dtype==1:#dissapearance type one: from black frog to exit
        for x in range(26,51):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
        frogmatic.destroy()
    if dtype==2:#dessapearance type two: from colourfull frog to exit
        for x in range(0,51):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
        frogmatic.destroy()
    if dtype==3:#dessapearance type two: from colourfull frog to black frog
        for x in range(0,27):
            img = PhotoImage(file='da_'+str(x)+'.gif')
            canvas.create_image(0,0, anchor=NW, image=img)
            frogmatic.update()
def position(xpos,ypos):#change position on the screen
    global frogmatic,canvas,img
    frogmatic.update_idletasks()
    width = frogmatic.winfo_width()
    height = frogmatic.winfo_height()
    x = ((frogmatic.winfo_screenwidth() // 100)*xpos) - (width // 2)
    y = ((frogmatic.winfo_screenheight() // 100)*ypos) - (height // 2)
    frogmatic.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    canvas.create_image(0,0, anchor=NW, image=img)
    frogmatic.update()
def gomono():#go monochromatic
    global frogmatic,canvas,img
    for x in range(20,120,20):
        img = PhotoImage(file='mono_'+str(x)+'.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        sleep(0.1)
        frogmatic.update()
def gounmono():#turn coulorfull
    global frogmatic,canvas,img
    for x in range(100,0,-20):
        img = PhotoImage(file='mono_'+str(x)+'.gif')
        canvas.create_image(0,0, anchor=NW, image=img)
        sleep(0.1)
        frogmatic.update()
def setsprite(sprite):#set to an additional sprite
    global frogmatic,canvas,img
    img = PhotoImage(file=sprite)
    canvas.create_image(0,0, anchor=NW, image=img)
    frogmatic.update()




#test all atributes
appear(1,90,90)
setsprite('nowifi.gif')
sleep(1)
position(50,50)
appear(2,90,90)
sleep(1)
appear(3,10,10)
sleep(1)
gomono()
gounmono()
appear(2,50,50)
disappear(1)
appear(2,50,50)
disappear(2)
appear(2,50,50)
disappear(3)
appear(2,50,50)
for x in range(1,100):
    position(x,x)
disappear(2)
##exit()
