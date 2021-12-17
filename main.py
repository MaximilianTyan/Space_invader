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
from tkinter import Canvas, Tk, Label, Button, PhotoImage

#Custom imports


#Window creation
wd=Tk()
wd.title("Space invaders")
wd.geometry("800x600+250+30")

txt1=Label(wd, text="Score : ")
txt2=Label(wd, text="Lives : ")

can=Canvas(wd, width=700, height=570, bg="blue")
earth= PhotoImage(file="image/earth.gif")
item=can.create_image(350,290,image=earth)

butonNew= Button(wd, text="New Game")
butonQuitt= Button(wd, text="QUIT", fg="red", command=wd.destroy)

txt1.grid(row=1, column=1, sticky="W")
txt2.grid(row=1, column=1, sticky="E")
can.grid(row=2, column=1)
butonNew.grid(row=2, column=2)
butonQuitt.grid(row=2, column=2, sticky="S")

wd.mainloop()