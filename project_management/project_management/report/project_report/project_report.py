# Copyright (c) 2013, Ravi Kharte and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data


def get_columns(filters):
	return[
		("Title of the Project") + ":Data:150"
		]

def get_data(filters):
	# conditions=get_conditions(filters)
	query=frappe.db.sql("""SELECT title_of_the_project from tabProject""")
	print("///////////////////////////////////////////////////////////", query)
	return query

	# def get_conditions(filters):
	# 	conditions = ""
	# 	# if filters.get("employee"): conditions += "employee = %(employee_name)s"
	# 	return conditions
