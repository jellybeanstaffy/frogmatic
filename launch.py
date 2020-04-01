##launcher v1.0.0
##component code 1
from tkinter import *
from time import sleep
from tkinter import messagebox
import urllib.request
def installer():
    try:
        r=urllib.request.urlopen('https://raw.githubusercontent.com/jellybeanstaffy/frogmatic/frogmatic/install.py')
        with open('install.dat','wb')as w:
            w.write(r.read())
            w.close()
        sleep(1)
        try:
            with open('install.dat','r')as r:
                exec(r.read())
                sleep(2)
            import frogmatic
            frogmatic.run()
            exit()
        except Exception as e:
            messagebox.showerror('frogmatic setup','an error has occurred, please relaunch the program')
            print('err:'+str(e))
            with open('database.dat','w')as w:
                w.write('ERRORCODE RUNTIME ATTEMPT REINSTALLATION')
                w.close()
            exit()
    except Exception as e:
        messagebox.showerror('frogmatic setup','the installer is unable to connect to the server. please check your internet connection.')
        print('err:'+str(e))
        sleep(2)
        exit()


##errorchecking before the program runs
try:
    with open('database.dat','r')as errorcheck:
        dat=errorcheck.read()
        errorcheck.close()
    if dat=='ERRORCODE RUNTIME ATTEMPT REINSTALLATION':
        print('err:previous execution failure')
        tk=Tk()
        tk.overrideredirect(True)
        tk.configure(bg='#fff')
        tk.wm_attributes("-transparentcolor",'#fff')
        messagebox.showinfo('frogmatic','a critical error occured last time you ran the program. please wait while the error is repiared')
        tk.destroy()
        installer()
except:
    pass

##if no errors found, run as nomal
try:
    import frogmatic
    frogmatic.run()
    exit()
except Exception as e:
    print('err:'+str(e))
    installer()
