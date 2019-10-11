#!/bin/python3
import mysql.connector
from tkinter import*
from PIL import ImageTk
import pyttsx3
import time
import tkinter.messagebox
import speech_recognition as sr
import textwrap
def o2(i,j):
    def sp3k():
        s=b.get()
        engine = pyttsx3.init()
        engine.say(s)
        print(s)
        engine.setProperty('rate',-20)  #120 words per minute
        engine.setProperty('volume',100) 
        engine.runAndWait()
  
    def wrap(s, w):
        return textwrap.fill(s, w)
    o2 = tkinter.Toplevel()
    b=StringVar()
    u=wrap(j,30)
    b.set(u)
    o2.title("RESULT")
    o2.geometry("400x400")
    #o2.resizable(width=False, height=False)
    o2.configure(bg="#27F207")

    label3 = Label(o2,text=f'You searched for :',bg="#27F207",bd=0,fg='#0D0D0D')
    label3.place(x=00,y=50)
    label3.config(font=("", 18))
    label4 = Label(o2,text=f'{i}',bg="#27F207",bd=0,fg='#0D0D0D')
    label4.place(x=100,y=90)
    label4.config(font=("Italic", 13))
    
    lab = Label(o2,text=f'RESULT :',bg="#27F207",bd=0,fg='#0D0D0D')
    lab.place(x=0,y=200)
    lab.config(font=("", 18))
    lab2 = Label(o2,text=f'{u}',bg="#27F207",bd=0,fg='#0D0D0D')
    lab2.place(x=10,y=240)
    lab2.config(font=("", 13),width=50)

    p2=ImageTk.PhotoImage(file="so.png")
    boton1 = Button(o2,image=p2,border=0,bg="#27F207",command=sp3k)
    boton1.place(x=330,y=195)
    o2.after(200, sp3k)
    time.sleep()

    o2.mainloop()

def cll():
    a=reco()
   
    msg1=tkinter.messagebox.askquestion('Info',f"You said : {a}")
    if msg1=='yes':
        s=info1(a) 
        o2(a,s)
         
    else :
        tkinter.messagebox.showerror('Error',"Please Retry")
    
    
def reco():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:

            print("Speak Anything :")
            r.energy_threshold = 4000
            r.pause_threshold=0.7
            audio = r.listen(source,timeout=10)

            print("trying to recgnize")
            text = r.recognize_google(audio)
            return text
                
    except:
        n="no result"
        print(n)
        

def info1(p):
    try :
        mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='guru1999')
        mycursor=mydb.cursor()

    except :
        print('not connected to database')


    mycursor.execute("USE py")
    mycursor.execute(f"select details from info where name='{p}'")
    # mycursor.execute("insert into ge2 values('guru')")
    for x in mycursor:
        try :
            aa = str(x).replace(')', '').replace('(', '').replace(',', '').replace("'", '')
            return aa
        except:
            tkinter.messagebox.showerror('Error',"Please Retry")
    mydb.commit()



o = tkinter.Tk()
c=StringVar()
o.title("PYTHON BOT")
o.geometry("500x500")
o.resizable(width=False, height=False)
o.configure(bg="#27F207")
#p=ImageTk.PhotoImage(file="bb.png")
#lbl=Label(o,image=p,bg='#27F207')
#lbl.place(x=330,y=350)

p1=ImageTk.PhotoImage(file="mic1.png")
boton = Button(o,image=p1,border=0,bg="#27F207",command=cll)
boton.place(x=200,y=200)

label = Label(o,text='Hello ! I am PYTHON BOT.\nYou can ask me anything about PYTHON.',bg="#27F207",bd=0,fg='#0D0D0D')
label.place(x=15,y=100)
label.config(font=("", 19))
label1 = Label(o,text='Tap to speak anything',bg="#27F207",bd=0,fg='#0D0D0D')
label1.place(x=160, y=300)
label1.config(font=("", 14))
o.mainloop()
