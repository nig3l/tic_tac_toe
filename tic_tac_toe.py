import tkinter as tk
from tkinter import font

class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Boaard game")
        self._cells = {}

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)




