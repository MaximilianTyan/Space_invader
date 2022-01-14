class Obstacle(Window):
    
    __list = []
    
    def __init__(self, pos_x, pos_y, size) -> None:
        self.__pos_x = pos_y
        self.__pos_y = pos_x
        self.__size = size
        
        self.__Sprite = self.create_image(self.__pos_x, self.__pos_y, 'images/missile.png', anchor='center', scale=1)
        
        Obstacle.__list.append(self)
    