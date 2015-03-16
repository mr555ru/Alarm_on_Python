# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
root = Tk()

def Time(event):
    lbl["text"] = datetime.datetime.now().time().strftime("%H:%M:%S") # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    
lbl = Label(root, text = " ", width=30,height=2, bg = "black", fg = "white")
lbl.pack()
btn = Button(root,                  #������������ ����
             text="Click me",       #������� �� ������
             width=30,height=5,     #������ � ������
             bg="white",fg="black") #���� ���� � �������
btn.bind("<Button-1>", Time)       #��� ������� ��� �� ������ ���������� ������� Time
btn.pack()                          #����������� ������ �� ������� ����
root.mainloop()