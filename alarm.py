# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
import pyglet
root = Tk()

def Time(event):
    lbl["text"] = datetime.datetime.now().time().strftime("%H:%M:%S") # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

def AlarmSound(event):
    sound = pyglet.resource.media('mlg.mp3')
    sound.play()

    
lbl = Label(root, text = " ", width=30,height=2, bg = "black", fg = "white")
lbl.pack()
btn = Button(root,                  #������������ ����
             text="Click me",       #������� �� ������
             width=30,height=5,     #������ � ������
             bg="white",fg="black") #���� ���� � �������
btn.bind("<Button-1>", Time)       #��� ������� ��� �� ������ ���������� ������� Time
btn.pack()                          #����������� ������ �� ������� ����
btn1 = Button(root,                 
             text="Click for MLG",       
             width=30,height=5,    
             bg="white",fg="black") 
btn1.bind("<Button-1>", AlarmSound)       
btn1.pack()  

root.mainloop()