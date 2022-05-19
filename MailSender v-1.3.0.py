from tkinter import *
import smtplib
from email.message import EmailMessage
import tkinter.messagebox as msbox

a=Tk()
#Title
a.title('Mail_Bot')
#Geometry
a.geometry("750x610")
a.minsize(750,610)
a.maxsize(750,610)
#MenuBar...
def Men():
    msbox.showinfo('Help','Hello User If you geting\nany problem Please find\nhelp.txt in the folder ')
M=Menu(a)
M.add_command(label='Help',command=Men)
a.config(menu=M)
#Title for GUI
Label(a,text='Mail sender...',font=('arial',15,'italic')).grid(row=0,column=1)
Label().grid(row=1)
#Username
Label(a,text='Username        ').grid(row=2)
U=StringVar()
Entry(a,textvariable=U,justify='center').grid(row=2,column=1)
#Senders data
Label().grid(row=3)
Label(a,text='Sender Mail-Id').grid(row=4)
Sid=StringVar()
Entry(a,textvariable=Sid,width=40,justify='center').grid(row=4,column=1)
Label().grid(row=4,column=2)
Label(a,text='Password   ').grid(row=4,column=3)
Sp=StringVar()
P=Entry(a,textvariable=Sp,show='*',justify='center')
P.grid(row=4,column=4)
def Show_p():
    if P.cget('show')=='*':
        P.config(show='')
    else:
        P.config(show='*')
C=Checkbutton(a,text='Show Password',command=Show_p)
C.grid(row=5,column=4)
#Reciveres data
Label().grid(row=5)
Label(a,text='Reciver Mail-Id').grid(row=6)
Rid=StringVar()
Entry(a,textvariable=Rid,width=40,justify='center').grid(row=6,column=1)
Label().grid(row=6,column=2)
#Subject
Label(a,text='Subject     ').grid(row=6,column=3)
Sub=StringVar()
Entry(a,textvariable=Sub,justify='center').grid(row=6,column=4)
#Message...
Label().grid(row=7)
Label(a,text='Message...        ').grid(row=8)
text=Text(a,width=50,height=20)
text.grid(row=9,column=1)
#Sending mail command
def send():
    msg=EmailMessage()
    msg['Subject']=f'{Sub.get()}'
    msg['From']=f'Mail_Bot'
    msg['To']=f'{Rid.get()}'
    msg.set_content(f'Username:{U.get()}\nMessage...\n\n{text.get(1.0,END)}')
    
    S=smtplib.SMTP_SSL('smtp.gmail.com',465)
    S.login(f'{Sid.get()}',f'{Sp.get()}')
    S.send_message(msg)
    Label(a,text='Mail Sent...',bg='black',fg='cyan').grid(row=10,column=3)
#Buttons & upcoming message...
Button(a,text='  Send  ',command=send,font=('arial',10)).grid(row=10,column=0)
#Button(a,text='  Quit  ',command=quit,font=('arial',10)).grid(row=10,column=1)
Label().grid(row=10,column=2)
Label(a,bg='black',text='            ').grid(row=10,column=3)
a.mainloop()
