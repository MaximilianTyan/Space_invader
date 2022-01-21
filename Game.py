#coding:utf-8

from random import randint

from Window import Window
from Bullet import Bullet
from Alien import Alien, FastAlien, NormalAlien, ToughAlien, HardAlien, Boss
from Spaceship import Spaceship
from Obstacle import Obstacle

class Game(Window):
    
    __playing = False
    __clock_time = 50
    
    @classmethod
    def create_window(cls):
        Window.link_functions(cls.start_game, cls.reset_game, cls.stop_game)
        Window.setup()
        Spaceship.setup()
    
    @classmethod
    def reset_game(cls):
        cls.get_Canvas().delete('all')
        cls.__score = 0
        cls.__level = 0
        
        Alien.reset()
        Bullet.reset()
        Spaceship.reset()
        
        cls.__formation = []
        cls.__front_row = []
        print('Game Reseted')
        
        cls.start_game()
    
    @classmethod
    def stop_game(cls):
        cls.__playing = False
        print('Game Stopped')
        
    @classmethod
    def start_game(cls):
        cls.__score = 0
        cls.__playing = True
        
        cls.__level = 0
        cls.level_init(cls.__level)
        cls.__prev_alien_count = Alien.get_alien_count()
        
        cls.clock()
        print('Game Started')
        
    
    @classmethod
    def clock(cls):
        
        #Entities ticks
        Bullet.tick()
        Alien.tick(cls.__formation, cls.__front_row)
        Spaceship.tick()
        
        #Score calculations
        diff = cls.__prev_alien_count - Alien.get_alien_count() 
        cls.__score += diff
        cls.__prev_alien_count  = Alien.get_alien_count()
        cls.disp_score(cls.__score)
        
        #End conditions
        alive = Spaceship.alive_check() and not Alien.bottom_check()
        win = Alien.win_check()
        
        if not alive:
            cls.lose()
        elif win:
            cls.win()
        
        
        if cls.__playing:
            cls.get_App().after(cls.__clock_time, cls.clock)
    
    @classmethod
    def level_init(cls, level):
        cls.bkg_image('images/earth.png')
        cls.spawn_ennemies(2,6)
   
    
    @classmethod
    def spawn_ennemies(cls, rows=1, cols=5, type=('normal')):
        
        dx = cls.get_Canvas().winfo_reqwidth() // (2 * (cols +2)) #Spawns alien only on one side of the screen to allow lateral movement
        dy = cls.get_Canvas().winfo_reqheight() // 10
        
        #print('max:', cls.get_Canvas().winfo_reqwidth(), cls.get_Canvas().winfo_reqheight(), 'div:', dx, dy)
        
        cls.__formation = []
        cls.__front_row = []
        
        for row in range(0, rows):
            row_list = []
            
            for col in range(0, cols):
                newAlien = NormalAlien(dx*(col+1), dy*(row+1))
                row_list.append(newAlien)
                
                if (row == rows - 1):
                    cls.__front_row.append(newAlien)
            cls.__formation.append(row_list)
        print('Ennemies Spawned')
        
    @classmethod
    def win(cls):
        x = cls.get_Canvas().winfo_reqwidth() // 2
        y = cls.get_Canvas().winfo_reqheight() // 2
        cls.__End_Sign = cls.get_Canvas().create_text(x, y, anchor='center', text="YOU WIN", fill="red", font=('Helvetica 50 bold'))
        cls.stop_game()
        print('You Win')
        
    @classmethod
    def lose(cls):
        x = cls.get_Canvas().winfo_reqwidth() // 2
        y = cls.get_Canvas().winfo_reqheight() // 2
        cls.__End_Sign = cls.get_Canvas().create_text(x, y, anchor='center', text="GAME OVER", fill="red", font=('Helvetica 50 bold'))
        cls.stop_game()
        print('You Lose')