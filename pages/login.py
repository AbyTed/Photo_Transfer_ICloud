import tkinter as tk
from tkinter import ttk

from .constants import LARGEFONT

class Login(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        
        
        # label of frame Layout 2
        label = ttk.Label(self, text="Login", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=3, padx=10, pady=10)

        button1 = ttk.Button(
            self, text="Home", command=lambda: controller.show_frame(pages['Home'])
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)