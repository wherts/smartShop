#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Tabs:
	def __init__(self, parent):
		self.root = Notebook(parent)
		self.frames = {}
		self.root.bind('<Button>', self.on_click)
		# self.frame1 = Frame(self.root)
		# self.root.add(self.frame1, text=label1)

		# self.frame2 = Frame(self.root)
		# self.root.add(self.frame2, text=label2)

		# self.frame3 = Frame(self.root)
		# self.root.add(self.frame3, text=label3)


	def add_frame(self, frame, label):
		# self.frames.append(frame)
		self.root.add(frame, text=label)
		print frame, label
		self.frames[label] = frame

	def get_root(self):
		return self.root

	def on_click(self, evt):
		print self.root.tabs()
		# print self.root.select()
		# print self.root.select()
		# print self.frames[self.root.select()]
