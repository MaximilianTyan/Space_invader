#coding:utf-8

from os import stat
from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage, StringVar

class Window():
    """
    Library of display functions inherited from by almost all object class
    to allow them to interact with the canvas without passing the Tk object
    as an attribute with each instancing 
    """
        
    #Init overrule
    def __init__(self) -> None:
            raise(Exception('Window class is not to be instanced, it is only for methods inheritance purposes'))
       
    @staticmethod
    def setup(width=800, height=600, offset_x=250, offset_y=30):
        """
        Creates the basic Window object

        Args:
            width (int, optional): [Window width in pixels]. Default to 800.
            height (int, optional): [Window height in pixels]. Default to 600.
            offset_x (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 250.
            offset_y (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 30.
        """
        Window.__App = Tk()
        
        Window.__App.title("Space invaders")
        Window.__App.geometry(f"{width}x{height}+{offset_x}+{offset_y}")


        Window.__Canvas = Canvas(Window.__App, width=700, height=570, bg="blue")
        
        #Battle Field
        Window.__Score_label = Label(Window.__App, text="Score : ")
        Window.__Lives_label = Label(Window.__App, text="Vies : ")

        
        #Title Screen
        Window.__New_Game_button= Button(Window.__App, text="NEW GAME")
        Window.__Exit_button= Button(Window.__App, text="QUITTER", fg="red", command=Window.__App.destroy)


        Window.layout_pack()
                
    @staticmethod   
    def create_image(pos_x, pos_y, image_source):
        Window.__tempImage= PhotoImage(file= image_source)
        return Window.__Canvas.create_image(pos_x, pos_y, image=Window.__tempImage)
    
    @staticmethod
    def layout_pack() -> None:
        Window.__Score_label.grid(row=1, column=1, sticky="W")
        Window.__Lives_label.grid(row=1, column=1, sticky="E")
        Window.__Canvas.grid(row=2, column=1)
        Window.__New_Game_button.grid(row=2, column=2)
        Window.__Exit_button.grid(row=2, column=2, sticky="S")
    
    @staticmethod
    def mainloop():
        print('loop')
        Window.__App.mainloop()
    
    
    # Getters
    @staticmethod
    def get_width() -> int:
        return Window.__App.width
    
    @staticmethod
    def get_height() -> int:
        return Window.__App.height
    
    @staticmethod
    def get_App() -> Tk:
        return Window.__App
    
    # Setters
    @staticmethod
    def disp_lives(lives) -> None:
        """
        Args:
            lives (int): new number of lives to be displayed
        """
        Window.__Lives_label.text = "Vies : " + str(lives)
    
    @staticmethod
    def disp_score(score) -> None:
        """
        Args:
            score (int): new score to be displayed
        """
        Window.__Score_label.text = "Vies : " + str(score)
    
    
