#coding:utf-8

from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage

class Window():
    """
    Custom wrapper inheriting from tkinter's Tk object to simplify interaction
    """
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
        self.__earth= PhotoImage(file="image/earth.gif")
        item=self.__Canvas.create_image(350,290, image=self.__earth)

        self.__New_Game_button= Button(self.__App, text="NEW GAME")
        self.__Exit_button= Button(self.__App, text="QUITTER", fg="red", command=self.__App.destroy)

        self.layout_pack()
        
    def layout_pack(self) -> None:
        self.__Score_label.grid(row=1, column=1, sticky="W")
        self.__Lives_label.grid(row=1, column=1, sticky="E")
        self.__Canvas.grid(row=2, column=1)
        self.__New_Game_button.grid(row=2, column=2)
        self.__Exit_button.grid(row=2, column=2, sticky="S")
    
    def mainloop(self):
        self.__App.mainloop()
    
    def get_width(self) -> int:
        return self.__App.width
    
    def get_height(self) -> int:
        return self.__App.height
    