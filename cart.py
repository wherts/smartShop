#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
import threading
import tkMessageBox

#custom classes
from receipt.receipt import Receipt, RemoveButton
from checkout.checkout import CheckoutButton
from header.header import Header
from tab.tablayout import Tabs
from scan.scan_page import Scan
from nutrition.nutrition_page import Nutrition
from search.search_page import Search

title = "SmartShop"
width = 700
height = 520
max_chars = 15
pane = tk.Tk()
pane.title(title)

curr_ndbno = -1

parent = tk.PanedWindow() #organizes receipt and widgets
parent.pack(fill=tk.BOTH, expand=1)


global queueName
global inQ
global t


def addToQueue(nameInQueue):
	global queueName 
	queueName = nameInQueue
	print "Added " + nameInQueue + " to the queue"
	
	# t.start()


	global inQ
	inQ = True
	checkQueue()
	


def removeFromQueue(nameInQueue):
	f = open("queue.txt","r+")
	lines = f.readlines()
	f.seek(0)
	for line in lines:
		if line != nameInQueue + "\n":
			f.write(line)
		else:
			print nameInQueue + " has been removed from queue"
	f.truncate()
	f.close()

	global inQ
	inQ = False


	title = "Dequeued"
	msg = "You (user#" + nameInQueue + ") have been removed from the queue. Happy SmartShopping!"
	
	tkMessageBox.showinfo(title, msg)

	global t
	# t = threading.Timer(5, checkQueue)
	t.cancel()



def checkQueue():
	global queueName, inQ, t
	if inQ:
	# 	t = threading.Timer(5, checkQueue).start()
	# else:
		f = open("queue.txt","r+")
		lines = f.readlines()
		f.seek(0)
		if len(lines) > 0:
			upNext = lines[0]
			numPeopleInQueue = 0
			for line in lines:
				numPeopleInQueue += 1
				if line == queueName + "\n":
					numInQueue = numPeopleInQueue

			print "next in line is " + upNext
			print "numPeople in queue: " + str(numPeopleInQueue)
			
			if queueName + "\n" == upNext:
				message = "You (" + queueName + ") are first in line! Please proceed to the checkout line now!"
				# global t
				# global T
				# t.cancel()
				# T = threading.Timer(15, checkQueue).start()
			else:

				message="There are " + str(numPeopleInQueue) + " people in line and you(" + queueName + ") are number " + str(numInQueue) +". You will be notified every 30 seconds on your queue status. Happy smartShopping!"
			tkMessageBox.showinfo("Queue status: ", message)
		f.close()
		global t
		try:
			t
		except NameError:
			t = threading.Timer(25, checkQueue)
			t.start()
		else:
			t = threading.Timer(25, checkQueue)
			t.start()
		
		


def callback():
	print "press"

def arrange_pane():
	sc_height = pane.winfo_screenheight()
	sc_width = pane.winfo_screenwidth()
	x = 0
	y = 0
	pane.geometry('%dx%d+%d+%d' % (width, height, x, y))

def setup_layout():
	receipt_container = tk.PanedWindow(parent, orient=tk.VERTICAL)
	receipt_container.pack()

	tabs = Tabs(parent)
	nutrition_tab = Nutrition(tabs.get_root())

	receipt = Receipt(parent, nutrition_tab)
	remove_button = RemoveButton(parent, receipt)
	CO_button = CheckoutButton(parent, receipt, addToQueue, removeFromQueue)
	receipt_container.add(receipt.get_root())
	receipt_container.add(remove_button.get_root())
	receipt_container.add(CO_button.get_root())

	scan_tab = Scan(tabs.get_root(), receipt)
	search_tab = Search(tabs.get_root())

	tabs.add_frame(scan_tab.get_root(), scan_tab.get_title())
	tabs.add_frame(nutrition_tab.get_root(), nutrition_tab.get_title())
	tabs.add_frame(search_tab.get_root(), search_tab.get_title())

	parent.add(receipt_container)
	parent.add(tabs.get_root())

	parent.pack()

	# receipt example
	# for i in range(4):
	# 	receipt.add_item("eggs", 3.99, {"Cholesterol": 5, "Sodium": 10})
	# for i in range(2):
	# 	receipt.add_item("cheese", 3.99, {"Cholesterol": 1, "Sodium": 12})
	# receipt.add_item("bacon", 5.99, {"Cholesterol": 4, "Sodium": 1000})
	# receipt.add_item("eggs", 3.99, {"Cholesterol": 2, "Sodium": 2400})

	# receipt.remove_item("cheese")
	# receipt.remove_item("cheese")

	# scan_tab.scan("049000032789") #poweraid
	# scan_tab.scan("020685084850") #cape cod chips



def main():
	arrange_pane()
	setup_layout()
	#always last
	pane.mainloop()



if __name__ == '__main__':
	main()
