#coding:utf-8

from Window import Window

from file_fct import *

class Obstacle(Window):
    
    __list = []
    __obstacle_count = 0
    
    __dir_x = 1
    __dir_y = 1
    
    debug = True
    
    
    def __init__(self, pos_x, pos_y, speed='none') -> None:
        
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
        
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, 'images/masque.png', anchor='center', scale=1)
        
        if Obstacle.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
        self.get_Canvas().tag_raise(self.__Sprite[0])
        
        Obstacle.__list.append(self)
        Obstacle.__obstacle_count += 1
    
    @classmethod
    def reset(cls):
        cls.__list = []
        cls.__obstacle_count = 0
        
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

    
    def take_damage(self, formation, front_row, damage=1):
        self._health -= damage
        
        if self._health <= 0:
            Obstacle.__list.remove(self)
            
            for row in formation:
                if self in row:
                    row.remove(self)
                    
            if self in front_row:
                front_row.remove(self)
                
            Obstacle.__obstacle_count -= 1
            
    
    
    def move(self, left_border_contact, right_border_contact):
        self.__pos_x = self.__pos_x + self.__speed * Obstacle.__dir_x
        if left_border_contact:
            self.__pos_y = self.__pos_y + self.get_Canvas().winfo_reqwidth() // 20
        elif right_border_contact:
            self.__pos_y = self.__pos_y + self.get_Canvas().winfo_reqwidth() // 20
        
        # Deletes the entity if its sprite exceeds graphical limits
        if self.__pos_y < 0 + self.__Sprite[1].height()//2:
            Obstacle.__list.remove(self)
            Obstacle.hit_bottom = True
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
            obstacle = suivant(Queue_left)
            if obstacle.__pos_x < 0 + obstacle.__Sprite[1].width()//2 :
                cls.__dir_x = 1
                left_border_contact = True
                break
        
        while not file_vide(Queue_right):
            obstacle = suivant(Queue_right)
            if obstacle.__pos_x > cls.get_Canvas().winfo_reqwidth() - obstacle.__Sprite[1].width()//2 :
                cls.__dir_x = -1
                right_border_contact = True
                break
                
        # Apply movement
        for row in formation:
            for instance in row:
                instance.move(left_border_contact, right_border_contact)
        