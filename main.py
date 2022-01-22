"""
Objectif : Réaliser une version custom de Space Invader en Python en utilisant la libairie graphique tkinter en POO
Date : 17/12/2021 - 
Fait par : Micheli Sebastien, Languille Antoine
TODO: 
- Bonus aléatoire
- Ajout son
"""

#Standard Imports
import time
#Custom imports
from Window import Window
from Game import Game

#Window creation
Game.create_window()
Game.start_game()
Window.mainloop()
