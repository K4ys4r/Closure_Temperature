#!/usr/bin/python
#-*- coding: UTF-8 -*-

try:
   from tkinter import *
except:
   from Tkinter import *

import math

def Analyse():
    try:
       TcCalc()
    except:
       can.coords(TcTxt,300,50)
       can.itemconfig(TcTxt,text='Check out if all variabeles are given!!',anchor=CENTER)

def Info():
    can.coords(TcTxt,300,50)
    can.itemconfig(TcTxt,text='This Python script calculates the Closure temperature by Dodson Formula.\nInput Variables: Ea, D0, Grain Size and Cooling Rate.\nExecution: python Tc_Calculation.pyc ',anchor=CENTER)


def TcCalc():
    Ea=float(eval(ent1.get()))
    D0=float(eval(ent2.get()))*1e-4
    a=float(eval(ent3.get()))*1e-6
    Cr=float(eval(ent4.get()))/(1e6*365*24*3600)
    R=8.31
    cte=50 # Spherical Form
    iT=1
    Test=False
    while not Test:
          tau=(R*iT*iT)/(Ea*Cr)
          Tc=Ea/(R*math.log(cte*tau*(D0/(a*a))))
          if iT==Tc:
             Test=True
          else:
             iT=Tc
    can.coords(TcTxt,300,50)
    can.itemconfig(TcTxt,text='The Closure Temperature is about:  :\n\n'+' '*25+str(round(Tc-273))+' °C',anchor=CENTER)



F=Tk()
F.title('.:: Closure Temperature Calculation by Dodson Formula ::.')
txt1=Label(F,text='Eff. Activation Energy ( Ea ~ J/mol ) :', font='Times 22 bold')
txt1.grid(row=0,sticky=W)
txt2=Label(F,text='Diffusion Coefficient (D0 ~ cm^2/s-1 ) :', font='Times 22 bold')
txt2.grid(row=1,sticky=W)
txt3=Label(F,text='Grain Size (a ~ µm ) :', font='Times 22 bold')
txt3.grid(row=2,sticky=W)
txt4=Label(F,text='Cooling Rate ( °C/Ma ):', font='Times 22 bold')
txt4.grid(row=3,sticky=W)

ent1 = Entry(F,width=20, font='Times 22 bold')
ent2 = Entry(F,width=20, font='Times 22 bold')
ent3 = Entry(F,width=20, font='Times 22 bold')
ent4 = Entry(F,width=20, font='Times 22 bold')
ent1.grid(row =0, column =1)
ent2.grid(row =1, column =1)
ent3.grid(row =2, column =1)
ent4.grid(row =3, column =1)

F.grid_columnconfigure(0, weight=1)
F.grid_rowconfigure(0, weight=1)

can=Canvas(F,width=400,height=100,bg='lightgrey')
can.grid(row=4,column=0,columnspan=4,sticky=EW)
TcTxt=can.create_text(20,10,fill='red',text='Please fill in the boxes with their corresponding values while taking into account their units..\nThen click Calculate Tc.',font='Times 22 bold',anchor=NW,width=580)


Cal=Button(F,text='Calculate Tc',font='Times 22 bold',command=Analyse)
Cal.grid(row=6,column=1)

Ref=Button(F,text='Info',font="Times 14 bold",command=Info)
Ref.grid(row=6,column=0)
F.mainloop()
