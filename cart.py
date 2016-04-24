#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook

#custom classes
from receipt.receipt import Receipt
from checkout.checkout import CheckoutButton
from header.header import Header
from tab.tablayout import Tabs
from scan.scan_page import Scan
from nutrition.nutrition_page import Nutrition
from search.search_page import Search

title = "SmartShop"
width = 700
height = 500
max_chars = 15
pane = tk.Tk()
pane.title(title)

curr_ndbno = -1

parent = tk.PanedWindow() #organizes receipt and widgets
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

	#just fill receipt to see it
	receipt = Receipt(parent)
	for i in range(12):
		receipt.add_item("eggs", 3.99)
	receipt_container.add(receipt.get_root())

	cobtn = CheckoutButton(parent, receipt)
	receipt_container.add(cobtn.get_root())

	tabs = Tabs(parent)
	scan = Scan(tabs.get_root())
	nutrition = Nutrition(tabs.get_root())
	search = Search(tabs.get_root())

	tabs.add_frame(scan.get_root(), scan.get_title())
	tabs.add_frame(nutrition.get_root(), nutrition.get_title())
	tabs.add_frame(search.get_root(), search.get_title())
	
	parent.add(receipt_container)
	parent.add(tabs.get_root())
	parent.pack()

	scan.scan(10009)

def main():
	arrange_pane()
	setup_layout()
	#always last
	pane.mainloop()


	# while True:
	# 	#check for scans
	# 	if curr_ndbno != -1:
			
	# 		pane.update_idletasks()
	#     	pane.update()


if __name__ == '__main__':
	main()