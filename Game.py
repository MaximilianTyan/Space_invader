#coding:utf-8

from random import randint

from Window import Window
from Bullet import Bullet
from Alien import Alien, FastAlien, NormalAlien, ToughAlien, HardAlien, Boss
from Spaceship import Spaceship
from Obstacle import Obstacle

class Game(Window):
    
    __playing = False
    __clock_time = 50 # soit 20 ticks par secondes
    __after_id = 0
    
    @classmethod
    def create_window(cls):
        Window.link_functions(cls.start_game, cls.reset_game, cls.stop_game)
        Window.setup()
        Spaceship.setup()
    
    @classmethod
    def reset_game(cls):
        cls.get_App().after_cancel(cls.__after_id)
        
        cls.get_Canvas().delete('all')
        cls.__score = 0
        cls.__level = 0
        
        Alien.reset()
        Bullet.reset()
        Spaceship.reset()
        
        cls.__alien_formation = []
        
        print('[Game Reseted]')
        cls.start_game()
    
    @classmethod
    def stop_game(cls):
        print('[Game Stopped]')
        cls.__playing = False
        cls.get_App().after_cancel(cls.__after_id)
        
        
    @classmethod
    def start_game(cls):
        print('[Game started]')
        cls.__score = 0
        cls.__playing = True
        
        cls.__level = 0  #Modifier ici le niveau auquel le jeu commence int [0:4]
        cls.level_init(cls.__level)
        cls.spawn_obstacles()
        
        cls.__prev_alien_count = Alien.get_alien_count()
        
        cls.clock()
        
        
    
    @classmethod
    def clock(cls):
        #Entities ticks
        Bullet.tick()
        Alien.tick(cls.__alien_formation)
        Obstacle.tick(cls.__obstacle_formation)
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
            cls.__level += 1
            
            if cls.__level >= 5:
                cls.win()
            else:
                cls.level_init(cls.__level)
        
        if cls.__playing:
            cls.__after_id = cls.get_App().after(cls.__clock_time, cls.clock)
    
    @classmethod
    def level_init(cls, level):
        cls.get_Canvas().delete('all')
        
        cls.__End_Sign = cls.get_Canvas().create_text(10, 10, anchor='nw', text="Level "+str(cls.__level+1), fill="white", font=('Helvetica 20 italic'))

        Alien.reset()
        Bullet.reset()
        Spaceship.reset(keeplives=True)
        Obstacle.reset(keepprevious=True)
        
        images = ['earth.png', 'mars.jpg', 'jupiter.jpeg','eye.jpg','pillars.jpg']
        cls.bkg_image('images/' + images[cls.__level])
        
        cls.spawn_mobs(level)
        #x = cls.get_Canvas().winfo_reqwidth() // 2
        #y = cls.get_Canvas().winfo_reqheight() // 2
        #a = HardAlien(x,y)
        #cls.__alien_formation = [[a]]
        #cls.__front_row = []
        
        cls.__prev_alien_count = Alien.get_alien_count()
        
    @classmethod
    def spawn_mobs(cls, level):
        
        width = cls.get_Canvas().winfo_reqwidth()
        height = cls.get_Canvas().winfo_reqheight()
        dy = width // 10
        
        x_offset = width // 5
        y_offset = height // 20
        
        level_ennemies = [
            ['NNN',],
            ['TNTNT',],
            ['NTTTN','FNNNF'],
            ['THHHT',],
            ['FBF','NTHTN']
        ]
        cls.__alien_formation = []
        for row, rows in enumerate(level_ennemies[level]):
            row_list = []
            for col, mob in enumerate(rows):
                dx = width // (len(rows) + 2)
                
                if mob == 'F':
                    newAlien = FastAlien(x_offset + dx*col, y_offset + dy*(row+1))
                elif mob == 'N':
                    newAlien = NormalAlien(x_offset + dx*col, y_offset + dy*(row+1))
                elif mob == 'T':
                    newAlien = ToughAlien(x_offset + dx*col, y_offset + dy*(row+1))
                elif mob == 'H':
                    newAlien = HardAlien(x_offset + dx*col, y_offset + dy*(row+1))
                
                if mob == 'B':
                    newAlien = Boss(width//2, height//4)
                    
                row_list.append(newAlien)
                
                    
            cls.__alien_formation.append(row_list)
        print(f'-- Lvl {cls.__level+1} ennemies spawned --')
            
   
    @classmethod
    def spawn_obstacles(cls, rows=2, cols=10, moving=False):

        width = cls.get_Canvas().winfo_reqwidth()
        height = cls.get_Canvas().winfo_reqheight()
        
        dx = width // (cols + 1) #Spawns alien only on one side of the screen to allow lateral movement
        dy = width // 20
        
        #print('max:', cls.get_Canvas().winfo_reqwidth(), cls.get_Canvas().winfo_reqheight(), 'div:', dx, dy)
        
        cls.__obstacle_formation = []
        
        y_offset = height - (height//5)
        
        for row in range(0, rows):
            row_list = []
            for col in range(0, cols):
                newObstacle = Obstacle(dx*(col+1), y_offset - dy*(row+1))
                row_list.append(newObstacle)
            cls.__obstacle_formation.append(row_list)
        print('-- Obstacles spawned --')
        
    @classmethod
    def win(cls):
        x = cls.get_Canvas().winfo_reqwidth() // 2
        y = cls.get_Canvas().winfo_reqheight() // 2
        cls.__End_Sign = cls.get_Canvas().create_text(x, y, anchor='center', text="YOU WIN", fill="green", font=('Helvetica 50 bold'))
        cls.stop_game()
        print('-= You Win =-')
        
    @classmethod
    def lose(cls):
        x = cls.get_Canvas().winfo_reqwidth() // 2
        y = cls.get_Canvas().winfo_reqheight() // 2
        cls.__End_Sign = cls.get_Canvas().create_text(x, y, anchor='center', text="GAME OVER", fill="red", font=('Helvetica 50 bold'))
        cls.stop_game()
        print('-= You Lost =-')