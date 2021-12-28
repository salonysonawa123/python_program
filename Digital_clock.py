from tkinter import Label,Tk

import time
from tkinter.constants import TOP

root = Tk()
root.title("DIGITAL CLOCK")

root.geometry("520x250")
root.resizable(0,0)

textfont = ("times romen",68,'bold')
bg = "#0CC0C7"      #background color
fg = "#3003F4"      #forground color
bd = 25        #border width



label = Label(root,font = textfont , background = bg , foreground=fg, border=bd ,pady=50, relief="groove" )
label.grid(row=5,column=1)



def digi_clock():
    tm = time.strftime("%H : %M : %S")
    label.config(text=tm)                 #config -> add extra value to label here we add text
    label.after(100,digi_clock)           #label.after(milisecond,funtion)
    


digi_clock()
root.mainloop()


