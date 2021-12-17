#coding:utf-8

class Alien():
    
    alien_count = 0
    
    def __init__(self, pos_x, pos_y, characteristics) -> None:
        self.x = pos_x
        self.y = pos_y
        
        Alien.alien_count += 1