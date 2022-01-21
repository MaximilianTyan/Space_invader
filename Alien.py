#coding:utf-8

from random import randint
from tkinter.constants import FALSE, S

from Window import Window
from Bullet import Bullet

from file_fct import *
class Alien(Window):
    
    __list = []
    __alien_count = 0
    
    __dir_x = 1
    __dir_y = 1
    
    debug = True
    
    hit_bottom = False
    
    def __init__(self, pos_x, pos_y) -> None:
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y

        if self.speed == 'slow':
            self.__speed = 3
        elif self.speed == 'normal':
            self.__speed = 5
        elif self.speed == 'fast':
            self.__speed = 10
        elif self.speed == 'none':
            self.__speed = 0
        else:
            self.__speed = 5
        
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self._image_src, anchor='center', scale=self._scale)
        
        if Alien.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
        self.get_Canvas().tag_raise(self.__Sprite[0])
        
        Alien.__list.append(self)
        Alien.__alien_count += 1
    
    @classmethod
    def reset(cls):
        cls.__list = []
        cls.__alien_count = 0
        
        cls.__dir_x = 1
        cls.__dir_y = 1
    
    @classmethod
    def get_alien_count(cls):
        return cls.__alien_count
    
    @classmethod
    def win_check(cls):
        return cls.get_alien_count() == 0
    
    @classmethod
    def bottom_check(cls):
        return cls.hit_bottom
    
    def shoot(self, speed='normal'): 
        Bullet(self.__pos_x, self.__pos_y, 'ennemy', speed)

    def detect_hit(self):
        x = self.__pos_x
        y = self.__pos_y
        
        x1 = x - self.__Sprite[1].width() //2 - self._hit_radius
        y1 = y - self.__Sprite[1].height() //2 - self._hit_radius
        
        width = self.__Sprite[1].width() + 2*self._hit_radius
        height = self.__Sprite[1].height() + 2*self._hit_radius
        
        if Alien.debug:
            self.get_Canvas().coords(self.__BoundingRect, x1, y1, x1+width, y1+height)
            
        detected = False
        
        for bullet in Bullet.get_list():
            if bullet.team == 'ally':   #player's bullet
                x1_b, y1_b, width_b, height_b = bullet.get_hitbox()
                
                # UP LEFT HAND CORNER
                if (x1 < x1_b < x1 + width)             and     (y1 < y1_b < y1 + height):
                    detected =  True
                    break
                
                # UP RIGHT HAND CORNER
                elif (x1 < x1_b + width_b < x1 + width) and     (y1 < y1_b < y1 + height):
                    detected = True
                    break
                
                # BOTTOM LEFT HAND CORNER
                elif (x1 < x1_b < x1 + width)           and     (y1 < y1_b + height_b < y1 + height):
                    detected = True
                    break
                
                # BOTTOM RIGHT HAND CORNER
                elif (x1 < x1_b + width_b < x1 + width) and     (y1 < y1_b + height_b < y1 + height):
                    detected = True
                    break
                
                else:
                    detected = False
        
        if detected:
            Bullet.get_list().remove(bullet)
        
        return detected

    
    def take_damage(self, formation, front_row, damage=1):
        self._health -= damage
        
        if self._health <= 0:
            Alien.__list.remove(self)
            
            for row in formation:
                if self in row:
                    row.remove(self)
                    
            if self in front_row:
                front_row.remove(self)
                
            Alien.__alien_count -= 1
            
    
    
    def move(self, left_border_contact, right_border_contact):
        self.__pos_x = self.__pos_x + self.__speed * Alien.__dir_x
        if left_border_contact:
            self.__pos_y = self.__pos_y + self.get_Canvas().winfo_reqwidth() // 20
        elif right_border_contact:
            self.__pos_y = self.__pos_y + self.get_Canvas().winfo_reqwidth() // 20
        
        # Deletes the entity if its sprite exceeds graphical limits
        if self.__pos_y < 0 + self.__Sprite[1].height()//2:
            Alien.__list.remove(self)
            Alien.hit_bottom = True
        else:
            self.get_Canvas().coords(self.__Sprite[0], self.__pos_x, self.__pos_y)
        
        
    @classmethod
    def tick(cls, formation, front_row):
        
        # Global border hit detection (change x directio of the formation)
        left_border_contact = False
        right_border_contact = False

        Queue_left = creer_file()
        Queue_right = creer_file()
        
        for row in formation:
            if len(row) != 0:
                Queue_left = ajouter(Queue_left, row[0])
                Queue_right = ajouter(Queue_right, row[-1])
        
        while not file_vide(Queue_left):
            alien = suivant(Queue_left)
            if alien.__pos_x < 0 + alien.__Sprite[1].width()//2 :
                cls.__dir_x = 1
                left_border_contact = True
                break
        
        while not file_vide(Queue_right):
            alien = suivant(Queue_right)
            if alien.__pos_x > cls.get_Canvas().winfo_reqwidth() - alien.__Sprite[1].width()//2 :
                cls.__dir_x = -1
                right_border_contact = True
                break
                
        # Apply movement
        for row in formation:
            for instance in row:
                instance.move(left_border_contact, right_border_contact)
        
        # Shoot attempt for the front_row
        if len(front_row) != 0 and randint(0,100) < 5:
            shooter_ind = randint(0, len(front_row) - 1)
            front_row[shooter_ind].shoot()
        
        # Damage detection
        
        for row in formation:
            for alien in row:
                if alien.detect_hit():
                    alien.take_damage(formation, front_row)

class FastAlien(Alien):
    def __init__(self, pos_x, pos_y, front_row=False) -> None:
        
        self._health = 1
        self.speed = 'fast'
        self._hit_radius = 20
        self._image_src = 'images/soucoupe.png'
        self._scale = 0.25
        super().__init__(pos_x, pos_y, front_row=front_row)

class NormalAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        
        self._health = 1
        self.speed = 'normal'
        self._hit_radius = 10
        self._image_src = 'images/karen.png'
        self._scale = 0.3
        
        super().__init__(pos_x, pos_y)

class ToughAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        self._health = 2
        self.speed = 'normal'
        self._hit_radius = 10
        self._image_src = 'images/trump.png'
        self._scale = 0.5
        
        super().__init__(pos_x, pos_y)

class HardAlien(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        self._health = 5
        self.speed = 'slow'
        self._hit_radius = 10
        self._image_src = 'images/raoult.png'
        self._scale = 1
        super().__init__(pos_x, pos_y)

        
class Boss(Alien):
    def __init__(self, pos_x, pos_y) -> None:
        self._health = 100
        self.speed = 'none'
        self._hit_radius = 10
        self._image_src = 'images/alien4.png'
        self._scale = 2
        super().__init__(pos_x, pos_y)

