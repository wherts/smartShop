#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
from item import Item

class Nutrition:
	height = 450
	width = 300
	upper_boundary = 30
	left_boundary = 20
	inner_boundary = 24
	rect_width = 430
	rect_height = 45
	rect_fill = "#888888"

	def __init__(self, parent):
		self.title = "Nutrition"
		self.root = Frame(parent)
		self.canvas = tk.Canvas(self.root, height=Nutrition.height, width=Nutrition.width)

		self.rects = {} #for holding the rectangles, indexed by nutrition type
		self.add_items()
		# self.update_rect(10, "Total Fat")
		# self.update_rect(10, "Saturated Fat")
		# self.update_rect(10, "Cholesterol")
		# self.update_rect(10, "Sodium")
		# self.update_rect(10, "Total carbohydrates")
		# self.add_to_rect(10, "Fiber")
		self.canvas.pack(fill=tk.BOTH)

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def add_items(self):
		left_x = Nutrition.left_boundary

		first_row_y = Nutrition.upper_boundary
		second_row_y = first_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		third_row_y = second_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		fourth_row_y = third_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		fifth_row_y = fourth_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		sixth_row_y = fifth_row_y + Nutrition.rect_height + Nutrition.inner_boundary

		self.rects["Total Fat"] = Item(self.canvas, "Total Fat", 65, left_x, first_row_y)
		self.rects["Saturated Fat"] = Item(self.canvas, "Sat Fat", 20, left_x, second_row_y)
		self.rects["Cholesterol"] = Item(self.canvas, "Cholesterol", 300, left_x, third_row_y)
		self.rects["Sodium"] = Item(self.canvas, "Sodium", 2400, left_x, fourth_row_y)
		self.rects["Total carbohydrates"] = Item(self.canvas, "Total Carbs", 300, left_x, fifth_row_y)
		self.rects["Dietary Fiber"] = Item(self.canvas, "Fiber", 25, left_x, sixth_row_y)

	def update_rect(self, amt, rect):
		self.rects[rect].update(amt)

# daily values:
		# Total fat - 65g (less than)
		# Sat fat - 20g (less than)
		# Cholesterol - 300mg (less than)
		# Sodium - 2400mg (less than)
		# Total Carb - 300 g (at least)
		# Fiber - 25 g (at least)
