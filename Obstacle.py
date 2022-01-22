#coding:utf-8

from Window import Window
from Bullet import Bullet
from file_fct import *

class Obstacle(Window):
    
    __list = []
    __obstacle_count = 0
    
    __dir_x = 1
    
    debug = False
    
    
    def __init__(self, pos_x, pos_y, speed='none') -> None:
        
        self._hit_radius = 0
        
        self.__pos_x = pos_x
        self.__pos_y = pos_y

        if speed == 'slow':
            self.__speed = 3
        elif speed == 'normal':
            self.__speed = 5
        elif speed == 'fast':
            self.__speed = 10
        elif speed == 'none':
            self.__speed = 0
        else:
            self.__speed = 5
        
        self._health = 1
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, 'images/masque.png', anchor='center', scale=0.07)
        
        if Obstacle.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
        
        Obstacle.__list.append(self)
        Obstacle.__obstacle_count += 1
    
    @classmethod
    def reset(cls, keepprevious=False):
        if not keepprevious:
            cls.__list = []
            cls.__obstacle_count = 0
        else:
            cls.restore_textures()
        cls.__dir_x = 1

    def detect_hit(self):
        x = self.__pos_x
        y = self.__pos_y
        
        x1 = x - self.__Sprite[1].width() //2 - self._hit_radius
        y1 = y - self.__Sprite[1].height() //2 - self._hit_radius
        
        width = self.__Sprite[1].width() + 2*self._hit_radius
        height = self.__Sprite[1].height() + 2*self._hit_radius
        
        if Obstacle.debug:
            self.get_Canvas().coords(self.__BoundingRect, x1, y1, x1+width, y1+height)
            
        detected = False
        
        for bullet in Bullet.get_list():
            if bullet.team == 'ennemy':   #alien's bullet
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

    @classmethod
    def restore_textures(cls):
        for obstacle in cls.__list:
            obstacle.restore_texture()
    
    def restore_texture(self):
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, 'images/masque.png', anchor='center', scale=0.07)
        
        if Obstacle.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
        
    def take_damage(self, formation, damage=1):
        self._health -= damage
        
        if self._health <= 0:
            Obstacle.__list.remove(self)
            
            for row in formation:
                if self in row:
                    row.remove(self)
                
            Obstacle.__obstacle_count -= 1
            
    
    
    def move(self):
        self.__pos_x = self.__pos_x + self.__speed * Obstacle.__dir_x
        
        # Deletes the entity if its sprite exceeds graphical limits
        if self.__pos_y < 0 + self.__Sprite[1].height()//2:
            Obstacle.__list.remove(self)
            Obstacle.hit_bottom = True
        else:
            self.get_Canvas().coords(self.__Sprite[0], self.__pos_x, self.__pos_y)
        
        
    @classmethod
    def tick(cls, formation):
        # Damage detection
        for row in formation:
            for obstacle in row:
                if obstacle.detect_hit():
                    obstacle.take_damage(formation)
            
        # Apply movement
        for row in formation:
            for instance in row:
                instance.move()
        