#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style

class RemoveButton:
	def __init__(self, parent, receipt):
		self.label = "Remove"
		self.receipt = receipt
		self.root = tk.Button(parent, text=self.label, command=self.on_click, padx=0, pady=0, bg="#e50000")

	def on_click(self):
		curr_entry = self.receipt.get_root().get(self.receipt.get_root().curselection())
		if curr_entry.split()[0] != "Total": 
			curr_item_name = self.receipt.get_name_from_entry(curr_entry)
			self.receipt.remove_item(curr_item_name)
		self.receipt.get_root().selection_clear(0)

	def get_root(self):
		return self.root

class Receipt:

	def __init__(self, parent, nutrition_tab, chars=18):
		self.root = tk.Listbox(parent, height=27, width=chars, bd=1)
		self.root.pack(fill=tk.BOTH)

		# dictionary where key = name, value = [index, price, count, nutrients]
		self.items = dict()
		# dictionary mapping the full entry to the item_name
		self.entries = dict()
		self.total = 0
		self.root.insert(0, "Total \t 0.00")
		self.nutrition_tab = nutrition_tab

	def add_item(self, item, price, nutrients):
		self.total += price
		item_name = str(item)
		pos = self.root.size()-1

		# if the item is already in the list, increment its count, otherwise simply add to the end of the list
		if self.items.has_key(item_name):
			self.items[item_name][2] += 1
			pos = self.items[item_name][0]
			self.root.delete(pos)
		else:
			self.items[item_name] = [pos, price, 1, nutrients]

		# formatting the entry for display: item_name x count, price
		entry = item_name + " x " + str(self.items[item_name][2]) + " \t " + str(price * self.items[item_name][2])
		self.root.insert(pos, entry)
		self.entries[entry] = item_name

		self.root.delete(self.root.size()-1)
		self.root.insert(self.root.size(), "Total \t\t " + str(self.total))

		#update nutrition tab
		for key in nutrients.keys():
			quantity = nutrients[key]
			self.nutrition_tab.update_rect(quantity, key)
			break

	def remove_item(self, item):
		item_name = str(item)
		nutrients = self.items[item_name][3]
		count = self.items[item_name][2]
		price = self.items[item_name][1]
		pos = self.items[item_name][0]
		entry = item_name + " x " + str(count) + " \t " + str(price * count)

		# update nutrients page
		for key in nutrients.keys():
			quantity = nutrients[key]
			self.nutrition_tab.update_rect(quantity * -1, key)

		# remove the item from the list
		self.root.delete(pos)

		# if it was the last item left then remove it from the list entirely
		if count == 1:
			self.items.pop(item_name)
			self.entries.pop(entry)
		#otherwise
		else:
			self.items[item_name][2] = count - 1
			entry = item_name + " x " + str(self.items[item_name][2]) + " \t " + str(price * self.items[item_name][2])
			self.root.insert(pos, entry)

		self.total -= price
		self.root.delete(self.root.size()-1)
		self.root.insert(self.root.size(), "Total \t\t " + str(self.total))

	def get_root(self):
		return self.root

	def get_total(self):
		return self.total

	def get_name_from_entry(self, entry):
		return self.entries[entry]

	def size(self):
		return self.root.size()-1
