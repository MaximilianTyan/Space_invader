#codong:utf-8

from Window import Window
from Bullet import Bullet
from pile_fct import creer_pile, depiler, pile_vide, taille_pile

class Spaceship(Window):
    
    debug = True
    
    @classmethod
    def setup(cls) -> None:
        cls.__lives = creer_pile(3)   #création d'une pile pour le nombre de vie 
        
        cls.__speed = 10
        
        cls.__pos_x = cls.get_Canvas().winfo_reqwidth() // 2
        cls.__pos_y = cls.get_Canvas().winfo_reqheight() * (1 - 0.1)
        
        cls.__Image = cls.create_image(cls.__pos_x, cls.__pos_y, 'images/anti-virus.png', anchor='center', scale = 0.3)
        if Spaceship.debug:
            cls.__BoundingRect = cls.get_Canvas().create_rectangle(0, 0, 
                                                                    cls.__Image[1].width(), 
                                                                    cls.__Image[1].height())
        
        key_dict = (
            (lambda evt: cls.left(), ('q', 'Left')),
            (lambda evt: cls.right(), ('d', 'Right')),
            (lambda evt: cls.shoot(), ('space',)),
        )
        for func,keys in key_dict:
            for key in keys:
                #print(f'', val[0])
                cls.get_App().bind(f'<{key}>', func)
    
    @classmethod
    def reset(cls):
        cls.setup()
    
    @classmethod  
    def left(cls) -> None:
        if cls.__pos_x > cls.__Image[1].width() //2 :
            cls.__pos_x -= cls.__speed
            cls.update_pos()
    
    @classmethod
    def right(cls) -> None:
        if cls.__pos_x < cls.get_Canvas().winfo_reqwidth() - cls.__Image[1].width() //2 :
            cls.__pos_x += cls.__speed
            cls.update_pos()
    
    @classmethod
    def shoot(cls):
        Bullet(cls.__pos_x, cls.__pos_y, 'ally', 'fast')
        cls.get_Canvas().tag_raise(cls.__Image[0])
    
    @classmethod
    def update_pos(cls):
        cls.get_Canvas().coords(cls.__Image[0], cls.__pos_x, cls.__pos_y)
        
        if Spaceship.debug:
            cls.get_Canvas().coords(cls.__BoundingRect, 
                                        cls.__pos_x - cls.__Image[1].width()//2,
                                        cls.__pos_y - cls.__Image[1].height()//2,
                                        cls.__pos_x + cls.__Image[1].width()//2, 
                                        cls.__pos_y + cls.__Image[1].height()//2)
    
    @classmethod       
    def alive_check(cls):
        return not pile_vide(cls.__lives)

    @classmethod
    def tick(cls):
        if cls.detect_hit(): 
            cls.__lives=depiler(cls.__lives)
        cls.disp_lives(taille_pile(cls.__lives))
    
    @classmethod
    def detect_hit(cls):
        
        x = cls.__pos_x
        y = cls.__pos_y
        
        x1 = x - cls.__Image[1].width() //2
        y1 = y - cls.__Image[1].height() //2
        
        width = cls.__Image[1].width()
        height = cls.__Image[1].height()
        
        if Spaceship.debug:
            cls.get_Canvas().coords(cls.__BoundingRect, x1, y1, x1+width, y1+height)
            
        detected = False
        
        for bullet in Bullet.get_list():
            if bullet.team == 'ennemy':   #player's bullet
                
                x1_b, y1_b, width_b, height_b = bullet.get_hitbox()
                
                # UP LEFT HAND CORNER
                if (x1 < x1_b < x1 + width) and (y1 < y1_b < y1 + height):
                    detected =  True

                    break
                
                # UP RIGHT HAND CORNER
                elif (x1 < x1_b + width_b < x1 + width) and (y1 < y1_b < y1 + height):
                    detected = True

                    break
                
                # BOTTOM LEFT HAND CORNER
                elif (x1 < x1_b < x1 + width) and (y1 < y1_b + height_b < y1 + height):
                    detected = True

                    break
                
                # BOTTOM RIGHT HAND CORNER
                elif (x1 < x1_b + width_b < x1 + width) and (y1 < y1_b + height_b < y1 + height):
                    detected = True
                    
                    break
                
                else:
                    detected = False
                
                
        if detected:
            Bullet.get_list().remove(bullet)
            
            cls.get_Canvas().create_oval(x1_b-10, y1_b-10, x1_b+10, y1_b+10, fill='red')
        
        return detected
        
