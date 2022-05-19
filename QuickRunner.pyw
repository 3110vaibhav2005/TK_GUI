import tkinter as tk
from tkinter import  filedialog, Text
import tkinter.messagebox as tmsg
import os
root=tk.Tk()




#Modification

root.title("QuickRunner")

#APPS not to be disturbed

apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    
    filename=filedialog.askopenfilename(initialdir="/", title="SelectFile",
                                        filetypes=(("executables", "*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame,text=app,bg='gold')
        label.pack()
def runApp():
    for app in apps:
        os.startfile(app)

#Canvas
canvas=tk.Canvas(root,height=600,width=600,bg="#263D42")
canvas.pack()
#Frame
frame=tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
#Buttons
def  msg_cmd():
    tmsg.showinfo("Help","To remove App inside it\ndelete save.txt from folder.")
H_B=tk.Button(root,text="Help",command=msg_cmd)
H_B.pack(side="left",anchor="n")
openFile=tk.Button(root,text="OpenFile",padx=10,pady=5,fg="white",bg='black',command=addApp)
openFile.pack()
runApps=tk.Button(root,text="RunApps",padx=10,pady=5,fg="White",bg='blue',command=runApp)
runApps.pack()

#version

l2=tk.Label(frame,text='v-1.1.0',font=('DS-DIGIB',7),fg='black')
l2.pack(anchor='ne')


for app in apps:
    label=tk.Label(frame,text=app)
    label.pack()



root.mainloop()


with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')
