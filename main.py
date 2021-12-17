"""
Objectif : Réaliser une version custom de Space Invader en Python en utilisant la libairie graphique tkinter en POO
Date : 17/12/2021 - 
Fait par : Micheli Sebastien, Languille Antoine
TODO: 
- Création et découpage de fenêtre
- Classe Alien
- Classe PlayerShip
- Classe Obstacles
- Score
- Collecte image (en cours)
"""

#Standard Imports
from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage

#Custom imports


#Window creation
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