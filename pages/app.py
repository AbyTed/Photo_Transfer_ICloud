import tkinter as tk
from tkinter import ttk



class App(tk.Tk):

    # __init__ function for class tkinterApp
	def __init__(self, pages, *args, **kwargs):

        # __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)

		# defining pages
		
		
        # creating a container
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in pages.values():

			frame = F(container, self, pages)


			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(pages['Login'])

		
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


