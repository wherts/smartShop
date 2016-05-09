#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Search:

	def __init__(self, parent):
		self.curr_search = ""
		self.title = "Search"
		self.root = Frame(parent)
		self.text = tk.Text(self.root, height=1, )
		self.text.bind("<Key>", self.build_word)
		self.text.bind("<Return>", self.lookup)
		self.text.pack()

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def build_word(self, event):
		self.curr_search += event.char
	
	# @param: upc is an identifier number that matches a specific item in the database
	def lookup(self, event):
		self.curr_search = ""
		print search
		if search is "":
			return 
		