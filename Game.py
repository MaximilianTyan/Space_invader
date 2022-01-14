#coding:utf-8

from random import randint

from Window import Window
from Bullet import Bullet
from Alien import Alien

class Game(Window):
    
    __playing = False
    __clock_time = 50
    
    @classmethod
    def game_reset(cls):
        cls.__level = 0
        cls.__score = 0
    
    @classmethod
    def stop_game(cls):
        cls.__playing = False
        
    @classmethod
    def start_game(cls):
        cls.__playing = True
        cls.clock()
    
    @classmethod
    def clock(cls):
        
        Alien.tick()
        Bullet.tick()
        
        if cls.__playing:
            cls.get_App().after(cls.__clock_time, cls.clock)
        