from tkinter import *
from tkinter.ttk import *
from time import strftime
#this fun is used to convert date time object to their string representation
root=Tk()
root.title("Clock")
def time():
    string = strftime('%H:%M:%S %p')
    #returns current time in string format 
    label.config(text=string)
    #text property changes
    label.after(1000,time)
    # the after() method to schedule an action that updates the current time to the label every second
label=Label(root,font=("ds-digital", 80), background="black",foreground="cyan")
label.pack(anchor='center')
time()
mainloop()