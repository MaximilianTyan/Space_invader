#coding:utf-8

from random import randint


from Bullet import Bullet
from Aliens import Alien

class Game():
    def __init__(self, Window) -> None:
        self.__Window = Window
        self.__clock_time = 50
    
    def new_game(self):
        self.__level = 0
    
    
    
    def clock(self):
        
        Aliens.tick()
        Bullets.tick()
        
        self.__Window.get_App().after(self.__clock_time, self.clock)
        