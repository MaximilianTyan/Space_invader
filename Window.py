#coding:utf-8

from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage, StringVar

class Window():
    """
    Custom wrapper inheriting from tkinter's Tk object to simplify interaction
    """
    
    #Creation & initialisation
    def __init__(self, width=800, height=600, offset_x=250, offset_y=30) -> None:
        """
        Creates the basic Window object

        Args:
            width (int, optional): [Window width in pixels]. Defaults to 800.
            height (int, optional): [Window height in pixels]. Defaults to 600.
            offset_x (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 250.
            offset_y (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 30.
        """
        self.__App = Tk()
        
        self.__App.title("Space invaders")
        self.__App.geometry(f"{width}x{height}+{offset_x}+{offset_y}")

        self.__Score_label = Label(self.__App, text="Score : ")
        self.__Lives_label = Label(self.__App, text="Vies : ")

        self.__Canvas = Canvas(self.__App, width=700, height=570, bg="blue")
        

        self.__New_Game_button= Button(self.__App, text="NEW GAME")
        self.__Exit_button= Button(self.__App, text="QUITTER", fg="red", command=self.__App.destroy)

        self.layout_pack()
    
    def create_image(self, pos_x, pos_y, image_source):
        self.__tempImage= PhotoImage(file= image_source)
        self.__Background_image = self.__Canvas.create_image(pos_x, pos_y, image=self.__tempImage)
    
    def layout_pack(self) -> None:
        
        self.__Score_label.grid(row=1, column=1, sticky="W")
        self.__Lives_label.grid(row=1, column=1, sticky="E")
        self.__Canvas.grid(row=2, column=1)
        self.__New_Game_button.grid(row=2, column=2)
        self.__Exit_button.grid(row=2, column=2, sticky="S")
        print('packed')
    
    def mainloop(self):
        print('loop')
        self.__App.mainloop()
    
    
    # Getters
    def get_width(self) -> int:
        return self.__App.width
    
    def get_height(self) -> int:
        return self.__App.height
    
    def get_App(self) -> Tk:
        return self.__App
    
    # Setters
    
    def disp_lives(self, lives) -> None:
        """
        Args:
            lives (int): new number of lives to be displayed
        """
        self.__Lives_label.text = "Vies : " + str(lives)
        
    def disp_score(self, score) -> None:
        """
        Args:
            score (int): new score to be displayed
        """
        self.__Score_label.text = "Vies : " + str(score)
    
    
