#codong:utf-8

from Window import Window
from Bullet import Bullet
class Spaceship(Window):
    
    def __init__(self) -> None:
        self.__lives = 3
        
        self.__speed = 10
        
        self.__pos_x = self.get_Canvas().winfo_reqwidth() // 2
        self.__pos_y = self.get_Canvas().winfo_reqheight() * (1 - 0.1)
        
        self.__Image = self.create_image(self.__pos_x, self.__pos_y, 'images/vaisseau.gif', anchor='center')
        
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
        
    