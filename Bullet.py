#coding:utf-8
from Window import Window
class Bullet(Window):
    
    __list = []
    
    def __init__(self, pos_x, pos_y, team='ennemy', speed='normal') -> None:
        """[summary]

        Args:
            pos_x (int): [description]
            pos_y (int): [description]
            team (str, optional): 'ennemy' / 'ally'. Defaults to 'ennemy'.
            speed (str, optional): 'slow' / 'normal' / 'fast'. Defaults to 'normal'.
        """
        self.__team = team
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        if self.__team == 'ally':
            self.__color = "yellow"
            self.__dir_y  = -1
        elif self.__team == 'ennemy':
            self.__color = "red"
            self.__dir_y = 1
        else:
            self.__color = 'red'
            self.__dir_y  = 1
        
        if speed == 'slow':
            self.__speed = 3
        elif speed == 'normal':
            self.__speed = 5
        elif speed == 'fast':
            self.__speed = 10
        else:
            self.__speed = 5
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, 'images/missile.png', anchor='center')
        
        Bullet.__list.append(self)

    @classmethod
    def tick(cls) -> None:
        for instance in cls.__list:
            # self.__pos_x = self.__pos_x + self.__speed * self.dir_y
            instance.__pos_y = instance.__pos_y + instance.__speed * instance.__dir_y
            
            if instance.__pos_y < 0 - instance.__Sprite[1].height()//2 :
                cls.__list.remove(instance)
            else:
                cls.get_Canvas().coords(instance.__Sprite[0], instance.__pos_x, instance.__pos_y)
        