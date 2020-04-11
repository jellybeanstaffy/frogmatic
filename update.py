##updater v1.0.0
from tkinter import *
from tkinter.ttk import *
from time import sleep
import urllib.request
import frank

print('##updater v1.0.0')
frank.bubble.say('##updater v1.0.0',0)

print('##fetch launch images')
frank.bubble.say('##fetch launch images',0)

for x in range(0,51):    
    try:
        with open('da_'+str(x)+'.gif','r')as r:
            r.close()
    except:
        r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/da_'+str(x)+'.gif')
        with open('da_'+str(x)+'.gif','wb')as w:
            w.write(r.read())
            w.close()
            
print('##fetch mono images')
frank.bubble.say('##fetch mono images',0)

for x in range(20,120,20):        
    try:
        with open('mono_'+str(x)+'.gif','r')as r:
            r.close()
    except:
        r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/mono_'+str(x)+'.gif')
        with open('mono_'+str(x)+'.gif','wb')as w:
            w.write(r.read())
            w.close()
            
print('##fetch status images')
frank.bubble.say('##fetch status images',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/nowifi.gif')
with open('nowifi.gif','wb')as w:
    w.write(r.read())
    w.close()
r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/searchingwifi.gif')
with open('searchingwifi.gif','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch icon')
frank.bubble.say('##fetch icon',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/frog.ico')
with open('frog.ico','wb')as w:
    w.write(r.read())
    w.close()
    
print('##fetch launcher')
frank.bubble.say('##fetch launcher',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/launch.py')
with open('launch.py','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch database')
frank.bubble.say('##fetch database',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/database.dat')
with open('database.dat','wb')as w:
    w.write(r.read())
    w.close()

print('##update version data')
frank.bubble.say('##fetch version data',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/version.dat')
with open('version.dat','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch main program')
frank.bubble.say('##fetch main program',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/frogmatic.py')
with open('frogmatic.py','wb')as w:
    w.write(r.read())
    w.close()
    
print('##fetch component: frank')
frank.bubble.say('##fetch component: frank',0)

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/frank.py')
with open('frank.py','wb')as w:
    w.write(r.read())
    w.close()
print('##done')
frank.bubble.say('done',2)
messagebox.showinfo('frogmatic update','update sucessfull')
