# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
root = Tk()

def Time(event):
    btn["text"] = datetime.datetime.now().time()

btn = Button(root,                  #������������ ����
             text="Click me",       #������� �� ������
             width=30,height=5,     #������ � ������
             bg="white",fg="black") #���� ���� � �������
btn.bind("<Button-1>", Time)       #��� ������� ��� �� ������ ���������� ������� Hello
btn.pack()                          #����������� ������ �� ������� ����
root.mainloop()