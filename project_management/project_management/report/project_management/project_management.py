# Copyright (c) 2013, Ravi Kharte and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data

def get_columns(filters):
	return[
		("Title of the Project") + ":Data:150",
		("Project ID") + ":Data:150",
		("Start date") + ":Data:150",
		("End date") + ":Data:150",
		("Status") + ":Data:150",
		("Total Resources working") + ":Data:150"
		]

def get_data(filters):
	# conditions=get_conditions(filters)
	query=frappe.db.sql("""SELECT a.title_of_the_project, b.project_id, b.start_date, b.end_date, b.status, a.total_resources_working FROM tabProject AS a, `tabProject Task` AS b WHERE a.project_id = b.project_id """)
	print("///////////////////////////////////////////////////////////", query)
	return query
