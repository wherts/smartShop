#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Scan:

	def __init__(self, parent):
		self.title = "Scan"
		self.root = Frame(parent)
		self.prompt = "Scan Item to Add\n it to Your Cart"
		self.label = tk.Label(self.root, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg="#E9E9E9", pady=170)
		self.label.pack()

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title