#coding:utf-8
from Window import Window
class Bullet(Window):
    
    __list = []
    debug = True
    
    def __init__(self, pos_x, pos_y, team='ennemy', speed='normal') -> None:
        """[summary]

        Args:
            pos_x (int): [description]
            pos_y (int): [description]
            team (str, optional): 'ennemy' / 'ally'. Defaults to 'ennemy'.
            speed (str, optional): 'slow' / 'normal' / 'fast'. Defaults to 'normal'.
        """
        self.team = team
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        if self.team == 'ally':
            self.__dir_y  = -1
            image_src = 'images/seringue.png'
            scale = 1
        else:
            image_src = 'images/virus.png'
            scale = 0.02
            
            self.__dir_y  = 1
        
        if speed == 'slow':
            self.__speed = 5
        elif speed == 'normal':
            self.__speed = 10
        elif speed == 'fast':
            self.__speed = 20
        else:
            self.__speed = 10
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, image_src, anchor='center', scale=scale)
        
        if Bullet.debug:
            self.__BoundingRect = self.get_Canvas().create_rectangle(0, 0, 
                                                                    self.__Sprite[1].width(), 
                                                                    self.__Sprite[1].height())
        
        Bullet.__list.append(self)
    
    @classmethod
    def reset(cls):
        cls.__list = []
    
    def get_hitbox(self):
        x = self.__pos_x
        y = self.__pos_y
        
        x1 = x - self.__Sprite[1].width() //2
        y1 = y - self.__Sprite[1].height() //2
        
        width = self.__Sprite[1].width() //2
        height = self.__Sprite[1].height() //2
        
        return x1, y1, width, height

    @classmethod
    def tick(cls) -> None:
        for instance in cls.__list:
            # self.__pos_x = self.__pos_x + self.__speed * self.dir_y
            instance.__pos_y = instance.__pos_y + instance.__speed * instance.__dir_y
            
            if instance.__pos_y < 0 - instance.__Sprite[1].height()//2 :
                cls.__list.remove(instance)
            else:
                cls.get_Canvas().coords(instance.__Sprite[0], instance.__pos_x, instance.__pos_y)
            
            if Bullet.debug:
                instance.get_Canvas().coords(instance.__BoundingRect, 
                                        instance.__pos_x - instance.__Sprite[1].width()//2,
                                        instance.__pos_y - instance.__Sprite[1].height()//2,
                                        instance.__pos_x + instance.__Sprite[1].width()//2, 
                                        instance.__pos_y + instance.__Sprite[1].height()//2)
    @classmethod
    def get_list(cls):
        return cls.__list