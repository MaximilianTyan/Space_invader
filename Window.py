#coding:utf-8

from tkinter import Canvas, Tk, Label, Button, Entry, PhotoImage, StringVar

class Window():
    """
    Custom wrapper inheriting from tkinter's Tk object to simplify interaction
    """
    
    #Creation & initialisation
    def __init__(Window, width=800, height=600, offset_x=250, offset_y=30) -> None:
        """
        Creates the basic Window object

        Args:
            width (int, optional): [Window width in pixels]. Defaults to 800.
            height (int, optional): [Window height in pixels]. Defaults to 600.
            offset_x (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 250.
            offset_y (int, optional): [Window offset from top right hand corner of the screen]. Defaults to 30.
        """
        Window.__App = Tk()
        
        Window.__App.title("Space invaders")
        Window.__App.geometry(f"{width}x{height}+{offset_x}+{offset_y}")
        
        Window.__Score_label = Label(Window.__App, text="Score :")
        Window.__Lives_label = Label(Window.__App, text="Vies :")

        Window.__Canvas = Canvas(Window.__App, width=550, height=550, bg="blue")
        #earth= PhotoImage(file="image/earth.jpg")
        #item=can.create_image(80,80, image=earth)

        Window.__Exit_button= Button(Window.__App, text="QUITTER", fg="red", command=Window.__App.destroy)

        Window.layout_pack()
        
    def layout_pack(Window) -> None:
        Window.__Score_label.grid(row=1, column=1)
        Window.__Lives_label.grid(row=1, column=2)
        Window.__Canvas.grid(row=2, column=1)
        Window.__Exit_button.grid(row=2, column=2)
    
    def mainloop(Window):
        Window.__App.mainloop()
    
    
    # Getters
    def get_width(Window) -> int:
        return Window.__App.width
    
    def get_height(Window) -> int:
        return Window.__App.height
    
    def get_App(Window) -> Tk:
        return Window.__App
    
    # Setters
    
    def disp_lives(Window, lives) -> None:
        """
        Args:
            lives (int): new number of lives to be displayed
        """
        Window.__Lives_label.text = "Vies : " + str(lives)
        
    def disp_score(Window, score) -> None:
        """
        Args:
            score (int): new score to be displayed
        """
        Window.__Score_label.text = "Vies : " + str(score)
    
    
