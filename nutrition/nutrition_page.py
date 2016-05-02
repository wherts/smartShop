#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Nutrition:
	height = 450
	width = 300
	outer_boundary = 20
	inner_boundary = 24
	rect_width = 430
	rect_height = 45

	def __init__(self, parent):
		self.title = "Nutrition"
		self.root = Frame(parent)
		self.canvas = tk.Canvas(self.root, bg="blue", height=Nutrition.height, width=Nutrition.width)
		self.canvas.pack(fill=tk.BOTH)
		self.rects = {}
		self.draw_rects()
		# remove_from_rect(10, "fiber")

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def draw_rects(self):
		left_x = Nutrition.outer_boundary

		first_row_y = Nutrition.outer_boundary
		second_row_y = first_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		third_row_y = second_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		fourth_row_y = third_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		fifth_row_y = fourth_row_y + Nutrition.rect_height + Nutrition.inner_boundary
		sixth_row_y = fifth_row_y + Nutrition.rect_height + Nutrition.inner_boundary

		cal_coor = left_x, first_row_y, left_x, first_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, first_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, first_row_y
		self.rects["calories"] = self.canvas.create_polygon(cal_coor, fill="black")

		sod_coor = left_x, second_row_y, left_x, second_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, second_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, second_row_y
		self.rects["sodium"] = self.canvas.create_polygon(sod_coor, fill="black")
		
		carbs_coor = left_x, third_row_y, left_x, third_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, third_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, third_row_y
		self.rects["carbs"] = self.canvas.create_polygon(carbs_coor, fill="black")
		
		fiber_coor = left_x, fourth_row_y, left_x, fourth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fourth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fourth_row_y
		self.rects["fiber"] = self.canvas.create_polygon(fiber_coor, fill="black")
		
		chol_coor = left_x, fifth_row_y, left_x, fifth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fifth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, fifth_row_y
		self.rects["cholesterol"] = self.canvas.create_polygon(chol_coor, fill="black")
		
		fat_coor = left_x, sixth_row_y, left_x, sixth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, sixth_row_y + Nutrition.rect_height, left_x + Nutrition.rect_width, sixth_row_y
		self.rects["fat"] = self.canvas.create_polygon(fat_coor, fill="black")

	def add_to_rect(self, amount, rect):
		pass

	def remove_from_rect(self, amount, rect):
		r = self.rects[rect]

# daily values:
		# Total fat - 65g (less than)
		# Sat fat - 20g (less than)
		# Cholesterol - 300mg (less than)
		# Sodium - 2400mg (less than)
		# Total Carb - 300 g (at least)
		# Fiber - 25 g (at least)