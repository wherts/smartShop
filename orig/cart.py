#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

#custom classes
from receipt import Receipt
from checkout import CheckoutButton
from header import Header
from tablayout import Tabs
from scan_page import Scan

title = "SmartShop"
width = 700
height = 500
max_chars = 15
pane = tk.Tk()
pane.title(title)

parent = tk.PanedWindow()
parent.pack(fill=tk.BOTH, expand=1)

def callback():
	print "press"

def arrange_pane():
	sc_height = pane.winfo_screenheight()
	sc_width = pane.winfo_screenwidth()
	x = 0
	y = sc_height/2
	pane.geometry('%dx%d+%d+%d' % (width, height, x, y))

def setup_layout():
	receipt_container = tk.PanedWindow(parent, orient=tk.VERTICAL)
	receipt_container.pack()

	receipt = Receipt(parent)
	for i in range(12):
		receipt.add_item("eggs", 3.99)
	receipt_container.add(receipt.get_root())

	cobtn = CheckoutButton(parent, receipt)
	receipt_container.add(cobtn.get_root())

	tabs = Tabs(parent)
	frame1 = Scan(tabs.get_root())
	# frame1 = Frame(tabs.get_root())
	frame2 = Frame(tabs.get_root())
	frame3 = Frame(tabs.get_root())

	tabs.add_frame(frame1.get_root(), frame1.get_title())
	tabs.add_frame(frame2, "Nutrition")
	tabs.add_frame(frame3, "Search")
	
	parent.add(Frame(parent))
	parent.add(receipt_container)
	parent.add(tabs.get_root())
	parent.pack()

def main():
	arrange_pane()
	setup_layout()

	#always last
	pane.mainloop()

if __name__ == '__main__':
	main()