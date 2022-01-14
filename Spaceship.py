#codong:utf-8

from Window import Window
from Bullet import Bullet
from Game import Game
from pile_fct import creer_pile, depiler, pile_vide
class Spaceship(Window):
    
    def __init__(self) -> None:
        self.__lives = creer_pile(3)   #création d'une pile pour le nombre de vie 
        
        self.__speed = 10
        
        self.__pos_x = self.get_Canvas().winfo_reqwidth() // 2
        self.__pos_y = self.get_Canvas().winfo_reqheight() * (1 - 0.1)
        
        self.__Image = self.create_image(self.__pos_x, self.__pos_y, 'images/vaisseau.gif', anchor='center')
        self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                self.__Image[1].width(), 
                                                                self.__Image[1].height())
        
        key_dict = (
            (lambda evt: self.left(), ('q', 'Left')),
            (lambda evt: self.right(), ('d', 'Right')),
            (lambda evt: self.shoot(), ('space',)),
        )
        for val in key_dict:
            for key in val[1]:
                #print(f'', val[0])
                self.get_App().bind(f'<{key}>', val[0])
        
    def left(self) -> None:
        if self.__pos_x > self.__Image[1].width() //2 :
            self.__pos_x -= self.__speed
            self.update_pos()
    
    def right(self) -> None:
        if self.__pos_x < self.get_Canvas().winfo_reqwidth() - self.__Image[1].width() //2 :
            self.__pos_x += self.__speed
            self.update_pos()
    
    def shoot(self):
        Bullet(self.__pos_x, self.__pos_y, 'ally', 'normal')
        print('pew')
    
    
    def update_pos(self):
        self.get_Canvas().coords(self.__Image[0], self.__pos_x, self.__pos_y)
        self.get_Canvas().coords(self.__BoundingRect, 
                                    self.__pos_x - self.__Image[1].width()//2,
                                    self.__pos_y - self.__Image[1].height()//2,
                                    self.__pos_x + self.__Image[1].width()//2, 
                                    self.__pos_y + self.__Image[1].height()//2)
        
    def life(self) :
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, self.__Image, anchor='center')
        x, y = self.get_Canvas().coords(self.__Sprite[0])
        
        x1 = x - self.__Sprite[1].width() //2 - self._hit_radius
        y1 = y - self.__Sprite[1].height() //2 - self._hit_radius
        
        x2 = x + self.__Sprite[1].width() //2 + self._hit_radius
        y2 = y + self.__Sprite[1].height() //2 + self._hit_radius
        
        detection = self.get_Canvas().find_overlapping(x1, y1, x2, y2)
        
        if len(detection)>4 : 
            self.__lives=depiler(self.__lives)
        if pile_vide(self.__lives)==True  : 
            Game.stop_game()
        
        self.disp_lives(len(self.__lives))
        
