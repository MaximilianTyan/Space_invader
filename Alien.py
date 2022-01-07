#coding:utf-8

from random import random

from Window import Window
from Bullet import Bullet

class Alien(Window):
    
    alien_count = 0
    list = []
    
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        Alien.__alien_count += 1
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        self.__dir_x = 1
        self.__dir_y = 1
        
        self.__front_row = front_row
    
    
    def shoot_attempt(self, speed='normal'):
        if self.__front_row:
            if random() < 0.25:
                self.shoot()
                Bullet(self.__pos_x, self.__pos_y, 'ennemy', speed)

    
    @classmethod
    def tick(cls):
        for instance in cls.list:
            instance.shoot_attempt()
            
            
            
            
        #print('alien tock')


class FastAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row) -> None:
        super().__init__(pos_x, pos_y, front_row)
        self.__health = 1
        self.__speed = 'fast'
        self.__hit_radius = 10
        self.__image = 'images/soucoupe.gif'
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')
        


class NormalAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row) -> None:
        super().__init__(pos_x, pos_y, front_row)
        self.__health = 1
        self.__speed = 'normal'
        self.__hit_radius = 10
        self.__image = 'images/alien.gif'
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')
        
        
        
class ToughAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row) -> None:
        super().__init__(pos_x, pos_y, front_row)
        
        self.__health = 2
        self.__speed = 'normal'
        self.__hit_radius = 15
        self.__image = 'images/alien5.gif'
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')

class HardAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row) -> None:
        super().__init__(pos_x, pos_y, front_row)
        
        self.__health = 5
        self.__speed = 'slow'
        self.__hit_radius = 10
        self.__image = 'images/alien3.gif'
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')


class Boss(Alien):
    def __init__(self, Window, pos_x, pos_y, front_row) -> None:
        super().__init__(Window, pos_x, pos_y, front_row)
        
        self.__health = 100
        self.__speed = 'none'
        self.__hit_radius = 10
        self.__image = 'images/alien4.gif'
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')