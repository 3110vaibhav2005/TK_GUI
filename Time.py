from tkinter import*
from tkinter.ttk import*
from time import strftime
a=Tk()
#icon
a.iconbitmap(r'C:\Users\VAIBHAV\Desktop\Python\App2\icon i.ico')
#title
a.title("Clock")
#time management
def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)


#label
label=Label(a,font=("ds-digital",80),background="Black",foreground="cyan")
label.pack(anchor="center")
#calling time
time()


a.mainloop()
