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

	tabs = Tabs(parent)
	nutrition_tab = Nutrition(tabs.get_root())

	receipt = Receipt(parent, nutrition_tab)
	CO_button = CheckoutButton(parent, receipt)
	receipt_container.add(receipt.get_root())
	receipt_container.add(CO_button.get_root())
	
	scan_tab = Scan(tabs.get_root(), receipt)
	search_tab = Search(tabs.get_root())

	tabs.add_frame(scan_tab.get_root(), scan_tab.get_title())
	tabs.add_frame(nutrition_tab.get_root(), nutrition_tab.get_title())
	tabs.add_frame(search_tab.get_root(), search_tab.get_title())
	
	parent.add(receipt_container)
	parent.add(tabs.get_root())

	parent.pack()

#	# receipt example
	for i in range(4):
		receipt.add_item("eggs", 3.99, {"Cholesterol": 5, "Sodium": 10})
	for i in range(2):
		receipt.add_item("cheese", 3.99, {"Cholesterol": 1, "Sodium": 12}) 
	receipt.add_item("bacon", 5.99, {"Cholesterol": 4, "Sodium": 1000})	
	receipt.add_item("eggs", 3.99, {"Cholesterol": 2, "Sodium": 2})

	receipt.remove_item("cheese")
	receipt.remove_item("cheese")


	# scan_tab.scan("049000032789") #poweraid
	# scan_tab.scan("020685084850") #cape cod chips


def main():
	arrange_pane()
	setup_layout()
	#always last
	pane.mainloop()



if __name__ == '__main__':
	main()