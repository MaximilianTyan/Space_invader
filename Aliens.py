#coding:utf-8

class Alien(Window):
    
    alien_count = 0
    
    def __init__(self, Window , pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y
        
        self.dir_x = 1
        self.dir_y = 1
        
        Alien.alien_count += 1
    
    def tick(self):
        print('alien tock')

class NormalAlien(Alien):
    def __init__(self, Window, pos_x, pos_y, characteristics) -> None:
        super().__init__(Window, pos_x, pos_y)