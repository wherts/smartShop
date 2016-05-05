#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
import urllib2
import json
import base64
import hashlib
import hmac
from receipt.receipt import Receipt

class Scan:

	def __init__(self, parent, receipt):
		self.curr_upc = ""
		self.receipt = receipt

		self.title = "Scan"
		self.root = Frame(parent)
		self.prompt = "Scan Item to Add\n it to Your Cart"
		self.label = tk.Label(self.root, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg="#E9E9E9", pady=170)
		self.text = tk.Text(self.root, height=1, )
		self.text.bind("<Key>", self.create_upc)
		self.text.bind("<Return>", self.scan(self.curr_upc))
		self.root.bind("<Visibility>", self.on_visibility)
		self.text.focus_set()
		self.text.pack()
		self.label.pack()


	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def create_upc(self, event):
		self.curr_upc += event.char

	def on_visibility(self, event):
		self.text.focus_set()

	# def callback(self, event):
	# 	self.scan(self.curr_upc)
	# 	self.curr_upc = ""

	def make_auth_token(self, upc_string):
		user_key = "Yt32S9a6l3Jq3Oc9"
		# user_key = "Dq92B9r0p7Zg5Pe9"
		m = hmac.new(user_key, upc_string, hashlib.sha1)
		return base64.b64encode(m.digest())

	# @param: upc is an identifier number that matches a specific item in the database
	def scan(self, upc):
		print upc
		if upc is "":
			return
		api_key = "/y1g77AYjOf/"
		# api_key = "/9ivKrAYSA60"

		signature = self.make_auth_token(upc)

		url = "http://digit-eyes.com/gtin/v2_0/?upc_code="+upc+"&app_key="+api_key+"&signature="+signature+"&language=en&field_names=description,formattedNutrition,image, thumbnail"
		data = json.load(urllib2.urlopen(url))
		print data
		return
		description = data["description"]
		nutrients = data["formattedNutrition"]

		#need to get pricing info from store

		servings = int(nutrients["Servings Per Container"]["qty"])
		servings = 2
		desired_nutrients = ["Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Total carbohydrates", "Dietary Fiber"]
		nutrients_amounts = dict()
		for key in nutrients.keys():
			if key in desired_nutrients:
				qty = int(str(nutrients[key]["qty"]).split()[0]) * servings
				print qty
				# dv = str(nutrients[key]["dv"])
				# newdv = dv.replace("%", "")
				# nutrients_amounts[key] = [qty, dv]
				nutrients_amounts[key] = qty

		receipt.add_item(description, 3.99, nutrients_amounts)

		#reset the upc code
		self.curr_upc = ""

#Sample Output
#		UPC: 020685084850
#		Calories from Fat, 110, DV: None
#		Sugars, 0 g, DV: None
#		Trans Fat, 0 g, DV: None
#		Sodium, 160 mg, DV: 7%
#		Iron, None, DV: 2%
#		Cholesterol, 0 mg, DV: 0%
#		Calories, 220, DV: None
#		Servings Per Container, 1, DV: None
#		Vitamin C, None, DV: 15%
#		Saturated Fat, 1 g, DV: 4%
#		Vitamin A, None, DV: 0%
#		Serving Size, 1.0 package, DV: None
#		Total Fat, 12 g, DV: 18%
#		Dietary Fiber, 2 g, DV: 7%
#		Protein, 3 g, DV: None
#		Calcium, None, DV: 0%
