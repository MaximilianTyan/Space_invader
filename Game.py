#coding:utf-8

from random import randint

from Window import Window
from Bullet import Bullet
from Alien import Alien

class Game(Window):
    def __init__(self) -> None:
        self.__clock_time = 50
    
    def game_reset(self):
        self.__level = 0
        self.__score = 0
    
    
    def clock(self):
        
        Alien.tick()
        Bullet.tick()
        
        self.get_App().after(self.__clock_time, self.clock)
        