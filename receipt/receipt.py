#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style

class Receipt:

	def __init__(self, parent, chars=18):
		self.root = tk.Listbox(parent, height=27, width=chars, bd=1)
		self.root.pack(fill=tk.BOTH)
		
		# dictionary where key = name, value = [index, price, count]
		self.items = dict()
		self.total = 0
		self.root.insert(0, "Total \t 0.00")

	def add_item(self, item, price):
		self.total += price
		item_name = str(item)
		pos = self.root.size()-1

		# if the item is already in the list, increment its count, otherwise simply add to the end of the list
		if self.items.has_key(item_name):
			self.items[item_name][2] += 1
			pos = self.items[item_name][0]
			self.root.delete(pos)
		else:
			self.items[item_name] = [pos, price, 1]
		
		entry = item_name + " x " + str(self.items[item_name][2]) + " \t " + str(price * self.items[item_name][2])
		self.root.insert(pos, entry)

		self.root.delete(self.root.size()-1)
		self.root.insert(self.root.size(), "Total \t\t " + str(self.total))

	def remove_item(self, item):
		item_name = str(item)
		count = self.items[item_name][2]
		price = self.items[item_name][1]
		pos = self.items[item_name][0]

		self.root.delete(pos)
		if count == 1:
			self.items.pop(item_name)
		else:
			self.items[item_name][2] = count - 1
			entry = item_name + " x " + str(self.items[item_name][2]) + " \t " + str(price * self.items[item_name][2])
			self.root.insert(pos, entry)

		self.total -= price

	def get_root(self):
		return self.root

	def get_total(self):
		return self.total

	def size(self):
		return self.root.size()-1