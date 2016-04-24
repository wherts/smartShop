#!/usr/bin/python
import Tkinter as tk
from ttk import Frame, Style, Notebook
import urllib2
import json

class Scan:

	# @param: parent is a TKinter Notebook 
	def __init__(self, parent):
		self.title = "Scan"
		self.root = Frame(parent)
		self.prompt = "Scan Item to Add\n it to Your Cart"
		self.label = tk.Label(self.root, text=self.prompt, font=("Helvetica", 26),anchor=tk.CENTER, bg="#E9E9E9", pady=170)
		self.label.pack()

	def get_root(self):
		return self.root

	def get_title(self):
		return self.title

	# @param: ndbno is an identifier number that matches a specific item in the database
	def scan(self, ndbno):
		
		# Query USDA database for the item indicated by ndbno 
		api_key = "sVAtymRKHlUt9DonsKD5UBLzoPRF6GeX0foDQQUb" # api_key issued to Ben Spector for access to USDA nutrition database 
		USDA_url = "http://api.nal.usda.gov/ndb/reports/?ndbno=" + str(ndbno) + "&type=b&format=json&api_key=" + api_key
		# json_data = urllib2.urlopen(USDA_url).read()
		data = json.load(urllib2.urlopen(USDA_url))
		food_name = data["report"]["food"]["name"]
		print food_name
		nutrients = data["report"]["food"]["nutrients"] #dict of nutrition facts for specified item
		
		# total fat, saturated fat, trans fat, cholesterol, sodium, total carbs
		# fiber, sugar, protein, Vitamin A, Vitamin C, Calcium, Iron

		desired_nutrients = ["Energy", "Protein", "Total lipid (fat)", "Carbohydrate, by difference","Fiber, total dietary","Sugars, total","Calcium, Ca","Iron, Fe","Sodium, Na","Fatty acids, total saturated","Fatty acids, total trans", "Cholesterol"]
		nutrients_report_list = []
		for i in range(0, len(nutrients)):
			curr_nutrient = nutrients[i]
			if curr_nutrient["name"] in desired_nutrients:
				nutrients_report_list.append(curr_nutrient)
				print curr_nutrient["name"]+ ": " + str(curr_nutrient["value"]) + " " + curr_nutrient["unit"]

		return nutrients_report_list

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

		

