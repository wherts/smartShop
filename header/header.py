#!/usr/bin/python
import Tkinter as tk
import tkMessageBox
from ttk import Frame, Style

class Header:
	color = "#90CAF9"

	def __init__(self, parent):
		self.root = tk.Frame(parent, bg=color)
		self.user = None

	def get_root():
		return self.label