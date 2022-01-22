#codong:utf-8

from Window import Window
from Bullet import Bullet
from pile_fct import creer_pile, depiler, pile_vide, taille_pile

class Spaceship(Window):
    
    debug = False
    
    @classmethod
    def setup(cls, lives='auto') -> None:
        
        if lives == 'auto':
            cls.__lives = creer_pile(3)   #création d'une pile pour le nombre de vie 
        else:
            cls.__lives = lives
        
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
        
        cls.__max_health = taille_pile(cls.__lives)
        cls.__cracked = False
        cls.__crack_image = None

        cls.__can_shoot = True
        cls.__shoot_cooldown = 0
        
        
    @classmethod
    def reset(cls, keeplives=False):
        if keeplives:
            lives = cls.__lives
        else:
            lives = 'auto'
        cls.setup(lives)
        
        if keeplives:
            cls.__lives = lives
            cls.update_cracks()
    
    @classmethod  
    def left(cls) -> None:
        if cls.__pos_x > cls.__Image[1].width() //2 :
            cls.__pos_x -= cls.__speed

    
    @classmethod
    def right(cls) -> None:
        if cls.__pos_x < cls.get_Canvas().winfo_reqwidth() - cls.__Image[1].width() //2 :
            cls.__pos_x += cls.__speed

    
    @classmethod
    def update_pos(cls):
        cls.get_Canvas().coords(cls.__Image[0], cls.__pos_x, cls.__pos_y)
        
        if cls.__cracked:
            cls.get_Canvas().coords(cls.__CrackSprite[0], cls.__pos_x, cls.__pos_y)
        
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
    def update_cracks(cls):
        perc = taille_pile(cls.__lives) / cls.__max_health 
        image = None
        
        if perc <= 0.25:
            image = 'images/impact_3.png'
        elif perc <= 0.50:
            image = 'images/impact_2.png'
        elif perc <= 0.75:
            image = 'images/impact_1.png'
            
        if image != cls.__crack_image:
            cls.__CrackSprite = cls.create_image(cls.__pos_x, cls.__pos_y, 
                                            image, anchor='center', scale=0.5)
            cls.__crack_image = image
            cls.__cracked = True
   
    @classmethod
    def shoot(cls):
        if cls.__can_shoot:
            Bullet(cls.__pos_x, cls.__pos_y, 'ally', 'fast')
            cls.get_Canvas().tag_raise(cls.__Image[0])
            
            if cls.__cracked:
                cls.get_Canvas().tag_raise(cls.__CrackSprite[0])
                
            cls.__shoot_cooldown = 10    # clock: 20Hz, i.e. 0.5s
            cls.__can_shoot = False

    @classmethod
    def tick(cls):
        cls.update_pos()
        cls.countdown()
        
        if cls.detect_hit(): 
            cls.__lives=depiler(cls.__lives)
            cls.update_cracks()
            
        cls.disp_lives(taille_pile(cls.__lives))
    
    @classmethod
    def countdown(cls):
        if cls.__shoot_cooldown > 0:
            cls.__shoot_cooldown -= 1
        else:
            cls.__can_shoot = True
    
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
                    
        return detected
        
