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
		# self.canvas.create_text(50, 50, text="0.0%")
		self.canvas.pack(fill=tk.BOTH)
		self.rects = {} #for holding the rectangles, indexed by nutrition type
		self.pcts = {} #for holding the percent labels, indexed by type of rectangle
		self.add_items()
		# self.update_rect(10, "fiber")
		# self.(self.root, text="0.0%", font=("Helvetica", 26),anchor=tk.CENTER, bg="#E9E9E9")
		# self.label.pack()
		self.add_to_rect(-100, "total_fat")

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

		self.rects["total_fat"] = Item(self.canvas, "Total Fat", 65, left_x, first_row_y)
		self.rects["sat_fat"] = Item(self.canvas, "Sat Fat", 20, left_x, second_row_y)
		self.rects["cholesterol"] = Item(self.canvas, "Cholesterol", 300, left_x, third_row_y)
		self.rects["sodium"] = Item(self.canvas, "Sodium", 2400, left_x, fourth_row_y)
		self.rects["carbs"] = Item(self.canvas, "Total Carbs", 300, left_x, fifth_row_y)
		self.rects["fiber"] = Item(self.canvas, "Fiber", 25, left_x, sixth_row_y)
		# sod_coor = left_x, second_row_y, left_x, second_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, second_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, second_row_y
		# self.rects["sodium"] = self.canvas.create_polygon(sod_coor, fill=Nutrition.rect_fill)
		#
		# carbs_coor = left_x, third_row_y, left_x, third_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, third_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, third_row_y
		# self.rects["carbs"] = self.canvas.create_polygon(carbs_coor, fill=Nutrition.rect_fill)
		#
		# fiber_coor = left_x, fourth_row_y, left_x, fourth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fourth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fourth_row_y
		# self.rects["fiber"] = self.canvas.create_polygon(fiber_coor, fill=Nutrition.rect_fill)
		#
		# chol_coor = left_x, fifth_row_y, left_x, fifth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fifth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fifth_row_y
		# self.rects["cholesterol"] = self.canvas.create_polygon(chol_coor, fill=Nutrition.rect_fill)
		#
		# fat_coor = left_x, sixth_row_y, left_x, sixth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, sixth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, sixth_row_y
		# self.rects["fat"] = self.canvas.create_polygon(fat_coor, fill=Nutrition.rect_fill)

	def add_to_rect(self, amt, rect):
		self.rects[rect].update(amt)

	# def update_rect(self, amount, rect):
	# 	r = self.rects[rect]
	# 	coordinates = self.canvas.coords(r)
	# 	self.canvas.delete(r)
	# 	print coordinates
	# 	for i in range(4, len(coordinates), 2):
	# 		coordinates[i] = coordinates[i] - amount
	# 	print coordinates
	# 	self.canvas.create_polygon(coordinates, fill=Nutrition.rect_fill)

# daily values:
		# Total fat - 65g (less than)
		# Sat fat - 20g (less than)
		# Cholesterol - 300mg (less than)
		# Sodium - 2400mg (less than)
		# Total Carb - 300 g (at least)
		# Fiber - 25 g (at least)
