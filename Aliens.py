#coding:utf-8

class Alien(Window):
    
    cls.__alien_count = 0
    
    def __init__(self, pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y
        
        self.dir_x = 1
        self.dir_y = 1
        
        Alien.__alien_count += 1
    
    def tick(self):
        print('alien tock')

class NormalAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        
        self.__health = 1
        self.__speed = 'normal'
        self.__hit_radius = 10
        self.__image = ''
        
class ToughAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        
        self.__health = 2
        self.__speed = 'normal'
        self.__hit_radius = 15
        self.__image = ''

class HardAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        
        self.__health = 5
        self.__speed = 'slow'
        self.__hit_radius = 10
        self.__image = ''


class HardAlien(Alien):
    def __init__(self, Window, pos_x, pos_y) -> None:
        super().__init__(Window, pos_x, pos_y)
        
        self.__health = 100
        self.__speed = 'none'
        self.__hit_radius = 10
        self.__image = ''