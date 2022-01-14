#coding:utf-8

from random import random
from tkinter.constants import FALSE, S

from Window import Window
from Bullet import Bullet


class Alien(Window):
    
    __alien_count = 0
    __list = []
    
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        Alien.__alien_count += 1
        
        self.debug = False
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        self.__dir_x = 1
        self.__dir_y = 1
        
        self.__front_row = front_row

        if self._speed == 'slow':
            self._speed = 3
        elif self._speed == 'normal':
            self._speed = 5
        elif self._speed == 'fast':
            self._speed = 10
        elif self._speed == 'none':
            self._speed = 0
        else:
            self._speed = 5
        
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self._image_src, anchor='center')
        
        if self.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
            self.__HitBox = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height(), fill='blue')
        
        Alien.__list.append(self)
    
    
    def shoot_attempt(self, speed='normal'): 
        if self.__front_row:
            if random() < 0.25:
                self.shoot()
                Bullet(self.__pos_x, self.__pos_y, 'ennemy', speed)

    def detect_hit(self):
        x1, y1 = self.get_Canvas().coords(self.__Sprite[0])
        x2 = x1 + self.__Sprite[1].width() //2
        y2 = y1 + self.__Sprite[1].height()//2
        detection = self.get_Canvas().find_overlapping(x1, y1, x2, y2)
        
        if self.debug:
            self.get_Canvas().coords(self.__HitBox, 
                                        self.__pos_x - self.__Sprite[1].width()//2,
                                        self.__pos_y - self.__Sprite[1].height()//2,
                                        self.__pos_x + self.__Sprite[1].width()//2, 
                                        self.__pos_y + self.__Sprite[1].height()//2)
        
        print(detection)
        
    @classmethod
    def tick(cls):
        for instance in cls.__list:
            instance.shoot_attempt()
            instance.detect_hit()
            
            instance.__pos_x = instance.__pos_x + instance._speed * instance.__dir_x
            
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
            
            if instance.debug:
                cls.get_Canvas().coords(instance.__BoundingRect, 
                                        instance.__pos_x - instance.__Sprite[1].width()//2,
                                        instance.__pos_y - instance.__Sprite[1].height()//2,
                                        instance.__pos_x + instance.__Sprite[1].width()//2, 
                                        instance.__pos_y + instance.__Sprite[1].height()//2)

class FastAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        
        self._health = 1
        self._speed = 'fast'
        self._hit_radius = 20,
        self._image_src = 'images/soucoupe.gif'
        
        super().__init__(pos_x, pos_y, front_row=front_row)

class NormalAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        
        self._health = 1
        self._speed = 'normal'
        self._hit_radius = 10,
        self._image_src = 'images/alien.gif'
        
        super().__init__(pos_x, pos_y, front_row=front_row)

class ToughAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 2
        self._speed = 'normal'
        self._hit_radius = 10,
        self._image_src = 'images/alien5.gif'
        
        super().__init__(pos_x, pos_y, front_row=front_row)

class HardAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 5
        self._speed = 'slow'
        self._hit_radius = 10,
        self._image_src = 'images/soucoupe.gif'
        super().__init__(pos_x, pos_y, front_row=front_row)

        
class Boss(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 100
        self._speed = 'none'
        self._hit_radius = 10,
        self._image_src = 'images/alien4.gif'
        
        super().__init__(pos_x, pos_y, front_row=front_row)

