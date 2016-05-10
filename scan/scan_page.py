#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
import re
import urllib2
import json
import base64
import io
import hashlib
import hmac
from receipt.receipt import Receipt

class Scan:
	bg_color = "#E9E9E9"

	def __init__(self, parent, receipt):
		self.curr_upc = ""
		self.receipt = receipt

		self.title = "Scan"
		self.root = Frame(parent)
		self.prompt = "Scan Item to Add\n it to Your Cart"
		self.label = tk.Label(self.root, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg=Scan.bg_color, pady=170)
		self.text = tk.Text(self.root, height=1, width=1, fg=Scan.bg_color, bg=Scan.bg_color, highlightcolor=Scan.bg_color, insertbackground=Scan.bg_color)
		self.text.bind("<Key>", self.create_upc)
		self.text.bind("<Return>", self.callback)
		self.root.bind("<Visibility>", self.on_visibility)
		self.text.focus_set()
		self.text.pack()
		self.label.pack()


	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def on_visibility(self, event):
		self.text.focus_set()

	def create_upc(self, event):
		self.curr_upc += event.char
		print self.curr_upc

	def callback(self, event):
		self.scan(self.curr_upc)
		self.curr_upc = ""

	# @param: upc is an identifier number that matches a specific item in the database
	def scan(self, upc):

		data = self.get_data(upc)

		description = data["description"]
		nutrients = data["formattedNutrition"]
		# curr_img_url = data["thumbnail"]

		print "Description: ", description
		print nutrients
		print "---------"

		#servings in item
		servings = 1
		# if "Servings Per Container" in nutrients: servings = float(nutrients["Servings Per Container"]["qty"])

		# pull out desired nutrients to be sent to receipt
		desired_nutrients = ["Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Total carbohydrates", "Dietary Fiber"]
		nutrients_amounts = dict()
		for key in nutrients.keys():
			if key in desired_nutrients:
				#splits quantity on numeric value
				qty = (re.findall(r'\d+|\D+', str(nutrients[key]["qty"]))[0])
				if qty == None:
					qty = 0
				else:
					qty = float(qty)
				nutrients_amounts[key] = qty * servings

				# dv = str(nutrients[key]["dv"])
				# newdv = dv.replace("%", "")
				# nutrients_amounts[key] = [qty, dv]

		# still need pricing data
		# add new item to receipt with description, price, nutrients
		self.receipt.add_item(description, 3.99, nutrients_amounts)

		# image_byt = urllib2.urlopen(curr_img_url).read()
		# image_b64 = base64.encodestring(image_byt)
		# photo = tk.PhotoImage(data=image_b64)
		# self.label = tk.Label(self.root, image=photo, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg=Scan.bg_color, pady=170)
		# self.label.image = photo
		# self.label.pack()

	def get_data(self, upc):
		print "UPC:", upc
		if upc is "":
			return

		# api_key = "/7LZow+CLrFl" #ioe.smartshop@gmail.com
		api_key = "/1i5tDRLniW0" #ioe.smartshop2@gmail.com
		# api_key = "/5L6JpJVLpCI"

		# user_key = "Gk93Y4w4e5Fl6Pe4" #ioe.smartshop@gmail.com
		user_key = "Ky74S9i9g1Jd7Qd1" #ioe.smartshop2@gmail.com
		# user_key = "Eb58I1n1j7Xj0By2"

		#create hashed signature based on user key
		m = hmac.new(user_key, upc, hashlib.sha1)
		signature = base64.b64encode(m.digest())

		url = "http://digit-eyes.com/gtin/v2_0/?upc_code="+upc+"&app_key="+api_key+"&signature="+signature+"&language=en&field_names=description,brand,formattedNutrition,image,thumbnail"
		data = json.load(urllib2.urlopen(url))

		return data
