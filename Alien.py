#coding:utf-8

from random import random

from Window import Window
from Bullet import Bullet


options = {
            'fast': {
                'health' : 1,
                'speed' : 'fast',
                'hit_radius' : 20,
                'image' : 'images/soucoupe.gif'
            },
            'normal': {
                'health' : 1,
                'speed' : 'normal',
                'hit_radius' : 10,
                'image' : 'images/alien.gif'
            },
            'tough': {
                'health' : 2,
                'speed' : 'normal',
                'hit_radius' : 10,
                'image' : 'images/alien5.gif'
            },
            'hard': {
                'health' : 5,
                'speed' : 'slow',
                'hit_radius' : 10,
                'image' : 'images/alien3.gif'
            },
            'boss': {
                'health' : 100,
                'speed' : 'none',
                'hit_radius' : 10,
                'image' : 'images/alien4.gif'
            }
        }


class Alien(Window):
    
    __alien_count = 0
    __list = []
    
    def __init__(self, pos_x, pos_y, type='normal', front_row=False) -> None:
        Alien.__alien_count += 1
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        self.__dir_x = 1
        self.__dir_y = 1
        
        self.__front_row = front_row

        if options[type]['speed'] == 'slow':
            self.__speed = 3
        elif options[type]['speed'] == 'normal':
            self.__speed = 5
        elif options[type]['speed'] == 'fast':
            self.__speed = 10
        elif options[type]['speed'] == 'none':
            self.__speed = 0
        else:
            self.__speed = 5
        
        self.__health = options[type]['health']
        self.__hit_radius = options[type]['hit_radius']
        self.__image = options[type]['image']
        
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__image, anchor='center')
        self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                self.__Sprite[1].width(), 
                                                                self.__Sprite[1].height())
        print(self.__BoundingRect)
        Alien.__list.append(self)
    
    
    def shoot_attempt(self, speed='normal'):
        if self.__front_row:
            if random() < 0.25:
                self.shoot()
                Bullet(self.__pos_x, self.__pos_y, 'ennemy', speed)

    def detect_hit(self):
        x1, y1 = self.get_Canvas().coords(self.__Sprite[0])
        x2 = x1 + self.__Sprite[1].width()
        y2 = y1 + self.__Sprite[1].height()
        detection = self.get_Canvas().find_overlapping(x1, y1, x2, y2)
        
        
    @classmethod
    def tick(cls):
        for instance in cls.__list:
            instance.shoot_attempt()
            instance.detect_hit()
            
            instance.__pos_x = instance.__pos_x + instance.__speed * instance.__dir_x
            
            if instance.__pos_x < 0 + instance.__Sprite[1].width()//2 :
                instance.__dir_x = 1
                instance.__pos_y = instance.__pos_y + cls.get_Canvas().winfo_reqwidth() // 20
            elif instance.__pos_x > cls.get_Canvas().winfo_reqwidth() - instance.__Sprite[1].width()//2 :
                instance.__dir_x = -1
                instance.__pos_y = instance.__pos_y + cls.get_Canvas().winfo_reqwidth() // 20
            
            # Deletes the entity if its sprite exceeds graphical limits
            if instance.__pos_y < 0 + instance.__Sprite[1].height()//2 :
                cls.__list.remove(instance)
            else:
                cls.get_Canvas().coords(instance.__Sprite[0], instance.__pos_x, instance.__pos_y)
            
            cls.get_Canvas().coords(instance.__BoundingRect, 
                                    instance.__pos_x - instance.__Sprite[1].width()//2,
                                    instance.__pos_y - instance.__Sprite[1].height()//2,
                                    instance.__pos_x + instance.__Sprite[1].width()//2, 
                                    instance.__pos_y + instance.__Sprite[1].height()//2)

