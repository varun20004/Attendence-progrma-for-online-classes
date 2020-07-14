import tkinter as tk
from tkinter import *
from tkinter import messagebox
import datetime
import os
absentes=["Hriday Makkar","Sanya Arora","Mayank Gangwani","Mikul Jain","Vedant Chavla","Varun Shama"]
p=0
root=tk.Tk()
root.geometry("300x400")
root.resizable(0,0)
root.title("Attendence record")
now = datetime.datetime.now()
Lab = Frame(root)
Lab.pack(expand = True, fill = "both")
r1 = Frame(root)
r1.pack(expand = True, fill = "both")
r2 = Frame(root)
r2.pack(expand = True, fill = "both")
r3 = Frame(root)
r3.pack(expand = True, fill = "both")
r4 = Frame(root)
r4.pack(expand = True, fill = "both")
r5 = Frame(root)
r5.pack(expand = True, fill = "both")
r6 = Frame(root)
r6.pack(expand = True, fill = "both")
sub = Frame(root)
sub.pack(expand = True, fill = "both")
def w():
    global p
    f=open(r"C:\Users\varun sharma\Desktop\Attendence program of class XII-F.txt","a")
    d=now.strftime("%d")
    p=str(p)
    m=now.strftime("%b %y")
    f.write("————————————————" + "\n" + "Date - " + d + " th " + m + "\n\nTotal Students - 6\n" + "Present - " + p + "\nAbsentees :->\n")
    for x in range (len(absentes)):
        y=x+1
        y=str(y)
        f.write(y + ".) " + absentes[x] + "\n")
    f.write("Frequently not Attending :->\n" + "————————————————\n")
    f.close
def sube():
    global absentes,h,s,m,mi,v,va,p
    h=h.get()
    s=s.get()
    m=m.get()
    mi=mi.get()
    v=v.get()
    va=va.get()
    if h==1:
        absentes.remove("Hriday Makkar")
        p=p+1
    if s==1:
        absentes.remove("Sanya Arora")
        p=p+1
    if m==1:
        absentes.remove("Mayank Gangwani")
        p=p+1
    if mi==1:
        absentes.remove("Mikul Jain")
        p=p+1
    if v==1:
        absentes.remove("Vedant Chavla")
        p=p+1
    if va==1:
        absentes.remove("Varun Shama")
        p=p+1
    w()
    root.quit()
    root.destroy()    
    os.startfile(r"C:\Users\varun sharma\Desktop\Attendence program of class XII-F.txt")
l="""Attendence record
of
class XII-f"""
lbl = Label(Lab,text = l,font = ("Freestyle Script", 20),bg="white")
lbl.pack(expand = True, fill = "both")

h=IntVar()
hriday=Checkbutton(r1,text = "1.) Hriday Makkar      ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=h)
hriday.pack(side = LEFT, expand = True, fill = "both",)

s=IntVar()
sanya=Checkbutton(r2,text = "2.) Sanya Arora           ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=s)
sanya.pack(side = LEFT, expand = True, fill = "both",)

m=IntVar()
mayank=Checkbutton(r3,text = "3.) Mayank Gangwani ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=m)
mayank.pack(side = LEFT, expand = True, fill = "both",)

mi=IntVar()
mikul=Checkbutton(r4,text = "4.) Mikul Jain              ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=mi)
mikul.pack(side = LEFT, expand = True, fill = "both",)

v=IntVar()
vedant=Checkbutton(r5,text = "5.) Vedant Chavla        ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=v)
vedant.pack(side = LEFT, expand = True, fill = "both",)

va=IntVar()
varun=Checkbutton(r6,text = "6.) Varun Shama         ",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,variable=va)
varun.pack(side = LEFT, expand = True, fill = "both",)

markattendence=Button(sub,text = "Submit",font = ("Lucida Handwriting", 15),relief = GROOVE,bg="white",border = 0,command=sube)
markattendence.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()