// Copyright (c) 2016, Ravi Kharte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Project Management"] = {
	"filters": [
		{
			"fieldname": "status",
			"label": __("Status"),
	    "fieldtype": "Select",
			"default":"New",
	    "options": ["New","WIP","Under QA","Completed"]
	  },
		{
			"fieldname": "title_of_the_project",
			"label": __("Title of the Project"),
	    "fieldtype": "Data"
		},
		{
	    "fieldname": "project_id",
	    "fieldtype": "Link",
	    "label": __("Project ID"),
	    "options": "Project",
	    "reqd": 1,
	    "unique": 1
	  },
	  {
      "fieldname": "start_date",
      "fieldtype": "Date",
      "label": __("Start date")
	  },
	  {
      "fieldname": "end_date",
      "fieldtype": "Date",
      "label": __("End date")
 		},
		{
			"fieldname": "total_resources_working",
     	"fieldtype": "Data",
     	"hidden": 1,
     	"label": __("Total Resources working")
	 	}

	]
};
