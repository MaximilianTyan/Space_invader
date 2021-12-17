"""
Objectif : Réaliser une version custom de Space Invader en Python en utilisant la libairie graphique tkinter en POO
Date : 17/12/2021 - 
Fait par : Micheli Sebastien, Languille Antoine
TODO: 
- Création et découpage de fenêtre
- Classe Alien
- Classe PlayerShip
- Classe Obstacles

"""

#Standard Imports
from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage

#Custom imports


#Window creation
wd=Tk()
wd.title("Space invaders")
wd.geometry("500x300+400+200")

butonQuitt= Button(wd, text="QUITTER", fg="red", command=wd.destroy)
butonQuitt.pack()

wd.mainloop()