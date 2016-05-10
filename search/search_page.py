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
		#configure parent for grid
		self.root.columnconfigure(0, weight=3)
		# self.root.columnconfigure(1, weight=2)
		self.root.columnconfigure(2, weight=1)

		self.text = tk.Text(self.root, height=1, width=50)
		self.text.bind("<Key>", self.build_word)
		self.text.bind("<BackSpace>", self.delete)
		self.text.bind("<Return>", self.lookup)
		# self.text.pack()
		self.build_dict()
		#spacing
		tk.Label(self.root, text="Search:", font=("Helvetica", 16), bg=Search.bg_color).grid(row=0, column=0)
		self.text.grid(row=0, column=1, columnspan=2)

	def build_dict(self):
		#specific item
		self.items["dorito"] = ["Doritos Nacho Cheese,$4.00,Aisle 5", "Doritos Cooler Ranch,$4.00,Aisle 5", "Doritos Pizza Flavored,$4.00,Aisle 5"]
		#search for brand
		self.items["kellogg's"] = ["Lucky Charms, $2.89, Aisle 3", "Cinnamon Toast Crunch, $3.00, Aisle 3", "Cocoa Puffs, $2.70, Aisle 3", "Raisin Bran, $4.00, Aisle 3"]
		#search for food type
		self.items["cereal"] = ["Lucky Charms, $2.89, Aisle 3", "Cinnamon Toast Crunch, $3.00, Aisle 3", "Cocoa Puffs, $2.70, Aisle 3", "Raisin Bran, $4.00, Aisle 3"]

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
		# self.labels = []
		for k in self.items.keys():
			if k.lower().startswith(self.curr_search):
				for i, t in enumerate(self.items[k]):
					# split_t = t.split(",")
					# for j in range(len(split_t)):
					tk.Label(self.root, text=t, font=("Helvetica", 14), bg=Search.bg_color, pady=5).grid(row=i+1, column=1)
		self.curr_search = ""
