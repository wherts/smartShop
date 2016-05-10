#!/usr/bin/python
import Tkinter as tk
import tkMessageBox
from ttk import Frame, Style
import urllib2
import random
import string

class CheckoutButton:

	def __init__(self, parent, receipt, addToQueueFunc, removeFromQueueFunc):
		self.label = "Checkout"
		self.receipt = receipt
		self.nameInQueue = None
		self.addToQueue = addToQueueFunc
		self.removeFromQueue = removeFromQueueFunc
		self.root = tk.Button(parent, text=self.label, command=self.on_click, padx=0, pady=0)

	def on_click(self):
		if self.label == "Remove from queue":
			self.remove()
		# elif self.receipt.size() < 1:
		# 	title = "Error with checkout"
		# 	msg = "Cart is empty!"
		else:
			with open("queue.txt", 'r+') as queueNum:
				self.nameInQueue = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
				print queueNum.read()

				queueNum.write(self.nameInQueue + "\n")
				queueNum.seek(0)
				for i, l in enumerate(queueNum):
					pass
				numPeopleInQueue = i + 1
				

				self.label = "Remove from queue"
				self.root.config(text='Remove from queue')
	
			self.addToQueue(self.nameInQueue)
			title = "Added to queue"
		

			tkMessageBox.showinfo(title, "You have been added to the queue! Number of people in queue: " + str(numPeopleInQueue))

	def remove(self):
		self.label = "Checkout"
		self.root.config(text="Checkout")
		self.removeFromQueue(self.nameInQueue)

	def get_root(self):
		return self.root