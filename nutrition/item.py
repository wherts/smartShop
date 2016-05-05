#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

class Item:
    rect_width = 430
    rect_height = 45
    rect_fill = "#888888"

    def __init__(self, canvas, title, total, x, y): #x, y are coordinates of top left
        self.canvas = canvas
        self.title = title #string, text label of rectangle
        self.current = 0.0
        self.total = float(total)  #max g/mg allowed
        self.x = x
        self.y = y

        #build item
        self.create_rect()
        self.draw_pct()
        self.create_label()

    def create_rect(self):
        self.coordinates = [self.x, self.y, self.x, self.y + Item.rect_height, self.x + 3, self.y + Item.rect_height, self.x + 1, self.y]
        self.rect = self.canvas.create_polygon(self.coordinates, fill=Item.rect_fill)

    def get_pct(self):
        return round((self.current / self.total) * 100, 2)

    def draw_pct(self):
        self.pct_offset = 8
        self.pct_label = self.canvas.create_text(self.x + self.pct_offset, self.y + (Item.rect_height / 2), text=str(self.get_pct()) + "%", font=("Helvetica", 18), anchor=tk.W)

    def create_label(self):
        self.label = self.canvas.create_text(self.x, self.y, text=self.title, font=("Helvetica", 16), anchor=tk.SW)

    def update(self, amt):
        #delete and read rectangle and text
    	self.canvas.delete(self.rect)
        self.canvas.delete(self.pct_label)
        #update current
        self.current += amt
        r = self.get_pct() / 100 #ratio
        y_offset = Item.rect_width * (r / 100.0)
    	for i in range(4, len(self.coordinates), 2):
    		self.coordinates[i] += y_offset
        #have to redraw rectangle and label
    	self.canvas.create_polygon(self.coordinates, fill=Item.rect_fill)
        self.draw_pct()
