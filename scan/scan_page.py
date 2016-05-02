#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
import urllib2
import json
import base64
import hashlib
import hmac

class Scan:
	
	
	# @param: parent is a TKinter Notebook 
	def __init__(self, parent):
		self.title = "Scan"
		self.root = Frame(parent)
		self.prompt = "Scan Item to Add\n it to Your Cart"
		self.label = tk.Label(self.root, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg="#E9E9E9", pady=170)
		self.text = tk.Text(self.root, height=1, )
		self.text.bind("<Key>", self.create_upc)
		self.text.bind("<Return>", self.callback)
		self.text.pack()
		self.label.pack()

		self.curr_upc = ""

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	def create_upc(self, event):
		self.curr_upc += event.char

	def callback(self, event):
		self.scan(self.curr_upc)
		self.curr_upc = ""	

	def make_auth_token(self, upc_string):
		m = hmac.new("Yt32S9a6l3Jq3Oc9", upc_string, hashlib.sha1)
		return base64.b64encode(m.digest())
	
	# @param: upc is an identifier number that matches a specific item in the database
	def scan(self, upc):
		
		api_key = "/y1g77AYjOf/"
		signature = self.make_auth_token(upc)
		# url = "http://digit-eyes.com/gtin/v2_0/?upc_code="+upc+"&app_key="+api_key+"&signature="+signature+"&language=en&field_names=description,uom,nutrition,formattedNutrition,image"
		url = "http://digit-eyes.com/gtin/v2_0/?upc_code="+upc+"&app_key="+api_key+"&signature="+signature+"&language=en&field_names=nutrition"
		data = json.load(urllib2.urlopen(url))
		nutrients = data["nutrition"].split()
		
		
		# total fat, saturated fat, trans fat, cholesterol, sodium, total carbs
		# fiber, sugar, protein, Vitamin A, Vitamin C, Calcium, Iron

		# desired_nutrients = ["Energy", "Protein", "Total lipid (fat)", "Carbohydrate, by difference","Fiber, total dietary","Sugars, total","Calcium, Ca","Iron, Fe","Sodium, Na","Fatty acids, total saturated","Fatty acids, total trans", "Cholesterol"]
		# nutrients_report_list = []
		
		# for i in range(0, len(nutrients)):
		# 	curr_nutrient = nutrients[i]
		# 	if curr_nutrient["name"] in desired_nutrients:
		# 		nutrients_report_list.append(curr_nutrient)
		# 		print curr_nutrient["name"]+ ": " + str(curr_nutrient["value"]) + " " + curr_nutrient["unit"]

		# return nutrients_report_list

		# daily values:
		# Total fat - 65g (less than)
		# Sat fat - 20g (less than)
		# Cholesterol - 300mg (less than)
		# Sodium - 2400mg (less than)
		# Total Carb - 300 g (at least)
		# Fiber - 25 g (at least)

		# energy_name = energy["name"] #string: value for name
		# energy_unit = energy["unit"] #string: unit name
		# energy_val = energy["value"] #int: quantity by unit

		

