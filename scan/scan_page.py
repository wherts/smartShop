#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Scan:

	def __init__(self, parent):
		self.title = "Scan"
		self.root = Frame(parent)

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title