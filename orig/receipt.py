#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style

class Receipt:

	def __init__(self, parent, chars=18):
		self.root = tk.Listbox(parent, height=27, width=chars, bd=1)
		self.root.pack(fill=tk.BOTH)

	def add_item(self, item, price):
		entry = str(item) + " " + str(price)
		pos = self.root.size()
		self.root.insert(pos, entry)

	def remove_item(self, item, count):
		print "removing", item

	def get_root(self):
		return self.root

	def size(self):
		return self.root.size()