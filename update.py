##updater v1.0.0
from tkinter import *
from tkinter.ttk import *
from time import sleep
import urllib.request

print('##updater v1.0.0')

print('##fetch launch images')

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

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/nowifi.gif')
with open('nowifi.gif','wb')as w:
    w.write(r.read())
    w.close()
r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/searchingwifi.gif')
with open('searchingwifi.gif','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch icon')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/frog.ico')
with open('frog.ico','wb')as w:
    w.write(r.read())
    w.close()
    
print('##fetch launcher')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/launch.py')
with open('launch.py','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch database')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/database.dat')
with open('database.dat','wb')as w:
    w.write(r.read())
    w.close()

print('##update version data')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/version.dat')
with open('version.dat','wb')as w:
    w.write(r.read())
    w.close()

print('##fetch main program')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/frogmatic.py')
with open('frogmatic.py','wb')as w:
    w.write(r.read())
    w.close()
    
print('##fetch component: bibblebobble')

r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/bibblebobble.py')
with open('bibblebobble.py','wb')as w:
    w.write(r.read())
    w.close()
print('##done')
messagebox.showinfo('frogmatic update','update sucessfull')
