#!/usr/bin/python
import Tkinter as tk
import tkMessageBox
from ttk import Frame, Style
import urllib2

class CheckoutButton:

	def __init__(self, parent, receipt):
		self.label = "Checkout"
		self.receipt = receipt
		self.root = tk.Button(parent, text=self.label, command=self.on_click, padx=0, pady=0)

	def on_click(self):
		title = "Alert"
		msg = "checkout time!"

		if self.receipt.size() < 1:
			msg = "cart is empty!"

		tkMessageBox.showinfo(title, msg)

	def get_root(self):
		return self.root