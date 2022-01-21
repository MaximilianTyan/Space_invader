#coding:utf-8

from random import random
from tkinter.constants import FALSE, S

from Window import Window
from Bullet import Bullet


class Alien(Window):
    
    __alien_count = 0
    __list = []
    
    __dir_x = 1
    __dir_y = 1
    
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        Alien.__alien_count += 1
        
        self.debug = False
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
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
        
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self._image_src, anchor='center', scale=self._scale)
        
        if self.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
            self.__HitBox = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height(), fill='blue')
        self.get_Canvas().tag_raise(self.__Sprite[0])
        
        Alien.__list.append(self)
        print('new alien',self.__pos_x, self.__pos_y, )
    
    
    def shoot_attempt(self, speed='normal'): 
        if self.__front_row:
            if random() < 0.25:
                self.shoot()
                Bullet(self.__pos_x, self.__pos_y, 'ennemy', speed)

    def detect_hit(self):
        x, y = self.get_Canvas().coords(self.__Sprite[0])
        
        x1 = x - self.__Sprite[1].width() //2 - self._hit_radius
        y1 = y - self.__Sprite[1].height() //2 - self._hit_radius
        
        x2 = x + self.__Sprite[1].width() //2 + self._hit_radius
        y2 = y + self.__Sprite[1].height() //2 + self._hit_radius
        
        detection = self.get_Canvas().find_overlapping(x1, y1, x2, y2)

        if self.debug:
            self.get_Canvas().coords(self.__HitBox, x1, y1, x2, y2)
        
        
    @classmethod
    def tick(cls, formation):
        
        left_border_contact = False
        right_border_contact = False

        for row in formation:
            for instance in row:
                if instance.__pos_x < 0 + instance.__Sprite[1].width()//2 :
                    cls.__dir_x = 1
                    left_border_contact = True
                    
                elif instance.__pos_x > cls.get_Canvas().winfo_reqwidth() - instance.__Sprite[1].width()//2 :
                    cls.__dir_x = -1
                    right_border_contact = True
        
        for row in formation:
            for instance in row:
                instance.shoot_attempt()
                instance.detect_hit()
                
                instance.__pos_x = instance.__pos_x + instance._speed * cls.__dir_x
                
                if left_border_contact:
                    instance.__pos_y = instance.__pos_y + cls.get_Canvas().winfo_reqwidth() // 20
                elif right_border_contact:
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
        self._hit_radius = 20
        self._image_src = 'images/soucoupe.png'
        self._scale = 0.25
        super().__init__(pos_x, pos_y, front_row=front_row)

class NormalAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        
        self._health = 1
        self._speed = 'normal'
        self._hit_radius = 10
        self._image_src = 'images/alien.png'
        self._scale = 0.3
        
        super().__init__(pos_x, pos_y, front_row=front_row)

class ToughAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 2
        self._speed = 'normal'
        self._hit_radius = 10
        self._image_src = 'images/alien5.png'
        self._scale = 0.5
        
        super().__init__(pos_x, pos_y, front_row=front_row)

class HardAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 5
        self._speed = 'slow'
        self._hit_radius = 10
        self._image_src = 'images/soucoupe.png'
        self._scale = 1
        super().__init__(pos_x, pos_y, front_row=front_row)

        
class Boss(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        self._health = 100
        self._speed = 'none'
        self._hit_radius = 10
        self._image_src = 'images/alien4.png'
        self._scale = 2
        super().__init__(pos_x, pos_y, front_row=front_row)

