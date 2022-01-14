#coding:utf-8

from random import randint

from Window import Window
from Bullet import Bullet
from Alien import Alien, FastAlien, NormalAlien, ToughAlien, HardAlien, Boss

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
        
        cls.spawn_ennemies(2,6)
        
        
        cls.clock()
    
    @classmethod
    def clock(cls):
        
        Alien.tick(cls.formation)
        Bullet.tick()
        
        if cls.__playing:
            cls.get_App().after(cls.__clock_time, cls.clock)
            
    @classmethod
    def spawn_ennemies(cls, rows=1, cols=5, type=('normal')):
        
        dx = cls.get_Canvas().winfo_reqwidth() // (2 * (cols +2)) #Spawns alien only on one side of the screen to allow lateral movement
        dy = cls.get_Canvas().winfo_reqheight() // 10
        
        print('max:', cls.get_Canvas().winfo_reqwidth(), cls.get_Canvas().winfo_reqheight(), 'div:', dx, dy)
        
        cls.formation = []
        for row in range(0, rows):
            row_list = []
            for col in range(0, cols):
                row_list.append(NormalAlien(dx*(col+1), dy*(row+1)))
            cls.formation.append(row_list)
        