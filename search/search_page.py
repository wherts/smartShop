#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Search:
	bg_color = "#E9E9E9"

	def __init__(self, parent):
		self.curr_search = ""
		self.title = "Search"
		self.items = {}
		self.root = Frame(parent)
		self.text = tk.Text(self.root, height=1, )
		self.text.bind("<Key>", self.build_word)
<<<<<<< HEAD
		self.text.bind("<BackSpace>", self.delete)
=======
>>>>>>> f219c49377601f9d7bb035567c9ea564ec5b4927
		self.text.bind("<Return>", self.lookup)
		self.text.pack()
		self.build_dict()
		self.labels = []

	def build_dict(self):
		#specific item
		self.items["dorito"] = ["Dorito Information: Name, Price, Aisle/Location"]
		#search for brand
		self.items["kellogg's"] = ["All of Kellogg's cereals", "Lucky Charms", "Cinnamon Toast Crunch"]
		#search for food type
		self.items["cereal"] = ["All cereals in the store"]

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def delete(self, event):
		if len(self.curr_search) > 0:
			self.curr_search = self.curr_search[:-1]

	def build_word(self, event):
		self.curr_search += event.char

	# @param: upc is an identifier number that matches a specific item in the database
	def lookup(self, event):
		print "here"
		print "Searching:", self.curr_search
		for k in self.items.keys():
			if k.lower().startswith(self.curr_search):
				for t in self.items[k]:
					self.labels.append(tk.Label(self.root, text=t, font=("Helvetica", 16), anchor=tk.NW, bg=Search.bg_color, justify=tk.LEFT, pady=5))
		self.add_info()
		self.curr_search = ""

	def add_info(self):
		for label in self.labels:
			label.pack()
