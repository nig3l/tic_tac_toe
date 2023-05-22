import tkinter as tk
from tkinter import font

#board creation
class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Boaard game")
        self._cells = {}

#display
    def _create_board_display(self):
        display_frame = tk.Frame(master=self) # to indicate the game's main window will be the frames' parent

        display_frame.pack(fill=tk.X) # for responsivenness of the window

        self.display = tk.Label(
            master = display_frame,
            text = "ready?",
            font=font.Font(size=28,weight="bold"),
        )
        self.display.pack()

#grid cells
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            


