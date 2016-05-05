#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Tabs:
	def __init__(self, parent):
		self.root = Notebook(parent)
		self.frames = {}
		# self.frame1 = Frame(self.root)
		# self.root.add(self.frame1, text=label1)

		# self.frame2 = Frame(self.root)
		# self.root.add(self.frame2, text=label2)

		# self.frame3 = Frame(self.root)
		# self.root.add(self.frame3, text=label3)


	def add_frame(self, frame, label):
		# self.frames.append(frame)
		self.root.add(frame, text=label)
		self.frames[label] = frame

	def get_root(self):
		return self.root
