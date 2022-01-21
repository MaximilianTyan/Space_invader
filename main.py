"""
Objectif : Réaliser une version custom de Space Invader en Python en utilisant la libairie graphique tkinter en POO
Date : 17/12/2021 - 
Fait par : Micheli Sebastien, Languille Antoine
TODO: 
- Classe obstacle
- Différents niveaux (hard code)
- Effets visuels dégâts (hit (> petit explosion))
- Propagation shoot après front_row
"""

#Standard Imports
import time
4
#Custom imports
from Window import Window
from Game import Game

#Window creation
Game.create_window()
print('Window created')
Game.start_game()
print('Initial game Started')
Window.mainloop()
