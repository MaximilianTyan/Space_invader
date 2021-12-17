#coding:utf-8

class Bullet(Window):
    
    def __init__(self, pos_x, pos_y:, team='ennemy', speed='normal') -> None:
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
            
        
        
        if self.speed == 'slow':
            self.__speed = None
        elif speed == 'normal':
            self.__speed = None
        elif speed == 'fast':
            self.__speed = None
        else :
            self.__speed = None
    
    def next_tick(self) -> None:
        # self.__pos_x = self.__pos_x + self.__speed * self.dir_y
        self.__pos_y = self.__pos_y + self.__speed * self.dir_y
    
    
    def tick(self):
        print('alien tock')