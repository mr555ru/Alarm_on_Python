# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
root = Tk()

def Time(event):
    now = datetime.datetime.now().time()
    btn["text"] = now.strftime("%H:%M:%S")  # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

btn = Button(root,                  #������������ ����
             text="Click me",       #������� �� ������
             width=30,height=5,     #������ � ������
             bg="white",fg="black") #���� ���� � �������
btn.bind("<Button-1>", Time)       #��� ������� ��� �� ������ ���������� ������� Hello
btn.pack()                          #����������� ������ �� ������� ����
root.mainloop()