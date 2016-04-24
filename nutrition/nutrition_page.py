#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Nutrition:
	height = 450
	width = 300
	outer_boundary = 40
	inner_boundary = 35
	circle_width = 110

	def __init__(self, parent):
		self.title = "Nutrition"
		self.root = Frame(parent)
		self.canvas = tk.Canvas(self.root, bg="blue", height=Nutrition.height, width=Nutrition.width)
		self.canvas.pack(fill=tk.BOTH)
		self.arcs = {}
		self.draw_arcs()

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def draw_arcs(self):
		left_col_x = Nutrition.outer_boundary
		middle_col_x = left_col_x + Nutrition.inner_boundary + Nutrition.circle_width
		right_col_x = middle_col_x + Nutrition.inner_boundary + Nutrition.circle_width
		
		first_row_y = Nutrition.outer_boundary
		# second_row_y = first_row_y + Nutrition.circle_width + Nutrition.boundary

		cal_coor = left_col_x, first_row_y, left_col_x + Nutrition.circle_width, first_row_y + Nutrition.circle_width
		self.arcs["calories"] = self.canvas.create_oval(cal_coor, fill="black")
		
		sod_coor = middle_col_x, first_row_y, middle_col_x + Nutrition.circle_width, first_row_y + Nutrition.circle_width
		self.arcs["sodium"] = self.canvas.create_oval(sod_coor, fill="black")
		
		carbs_coor = right_col_x, first_row_y, right_col_x + Nutrition.circle_width, first_row_y + Nutrition.circle_width
		self.arcs["carbs"] = self.canvas.create_oval(carbs_coor, fill="black")
		
		# fiber_coor = right_col_x, second_row_y, right_col_x + Nutrition.circle_width, second_row_y + Nutrition.circle_width
		# self.arcs["fiber"] = self.canvas.create_oval(fiber_coor, fill="black")
		
		# chol_coor = 0, 0, 0, 0
		# self.arcs["cholesterol"] = self.canvas.create_oval(chol_coor, fill="black")
		
		# fat_coor = 0, 0, 0, 0
		# self.arcs["fat"] = self.canvas.create_oval(fat_coor, fill="black")
		# coord = 50, 50, 50, 50
		# arc = self.canvas.create_arc(coord, start=0, extent=359, fill="red")


# daily values:
		# Total fat - 65g (less than)
		# Sat fat - 20g (less than)
		# Cholesterol - 300mg (less than)
		# Sodium - 2400mg (less than)
		# Total Carb - 300 g (at least)
		# Fiber - 25 g (at least)