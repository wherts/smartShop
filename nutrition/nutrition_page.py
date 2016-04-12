#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Nutrition:

	def __init__(self, parent):
		self.title = "Nutrition"
		self.root = Frame(parent)
		# self.canvas = 

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title