"""
objectif : 
date : 17/12/2021
fait par : Micheli Sebastien, Languille Antoine
a faire : 
"""

from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage

wd=Tk()
wd.title("Space invaders")
wd.geometry("800x600+250+30")

txt1=Label(wd, text="Score : ")
txt2=Label(wd, text="Vies : ")

can=Canvas(wd, width=550, height=550, bg="blue")
#earth= PhotoImage(file="image/earth.jpg")
#item=can.create_image(80,80, image=earth)

butonQuitt= Button(wd, text="QUITTER", fg="red", command=wd.destroy)

txt1.grid(row=1, column=1)
txt2.grid(row=1, column=2)
can.grid(row=2, column=1)
butonQuitt.grid(row=2, column=2)

wd.mainloop()