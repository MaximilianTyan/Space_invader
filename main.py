"""
objectif : 
date : 17/12/2021
fait par : Micheli Sebastien, Languille Antoine
a faire : 
"""

from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage

wd=Tk()
wd.title("Space invaders")
wd.geometry("500x300+400+200")

butonQuitt= Button(wd, text="QUITTER", fg="red", command=wd.destroy)
butonQuitt.pack()

wd.mainloop()