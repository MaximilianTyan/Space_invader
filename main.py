"""
Objectif : Réaliser une version custom de Space Invader en Python en utilisant la libairie graphique tkinter en POO
Date : 17/12/2021 - 
Fait par : Micheli Sebastien, Languille Antoine
TODO: 
- Classe Alien (et les levels en général)
- Classe PlayerShip (mouvement, tirs...)
- Classe Obstacles
- Score
- Collecte image (en cours)
- Hitbox detection
- Différents écrans (Window \in CrtScreen \in {Boutons, objets, titres...})
"""

#Standard Imports
import time

#Custom imports
from Window import Window
from Spaceship import Spaceship
from Game import Game
from Alien import FastAlien, NormalAlien, ToughAlien, HardAlien, Boss

#Window creation
Window.setup()

x = NormalAlien(Window.get_Canvas().winfo_reqwidth()//2, Window.get_Canvas().winfo_reqheight()//2)

Player = Spaceship()
Game.start_game()






Window.mainloop()
    
    
    
    
    
    
    
