# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ravi Kharte and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProjectTask(Document):
	def on_update(self):
		doc = frappe.get_doc("Project",self.project_id)
		# doc.total_resources_working =

		if self.status == "WIP":
			user_roles = frappe.get_roles(frappe.session.user)

			doc.total_resources_working = user_roles
			doc.save()


		#
		# user_doc = frappe.get_doc("User",{"name":frappe.session.user})
		# doc.total_resources_working.append(user_doc.first_name)
		# doc = frappe.get_doc("Project",self.project_id)
		# doc.total_resources_working = []
		# doc.save()
		# if self.status == "New":
		# 	project = frappe.get_doc("Project",self.project_id)
		# 	project.total_resources_working = self.count
			# total_resources_working.save()
		# elif self.status == "WIP":
		# 	project = frappe.get_doc("Project",self.project_id)
		# 	project.total_resources_working = self.count + 1
		# elif self.status == "Under QA":
		# 	project = frappe.get_doc("Project",self.project_id)
		# 	project.total_resources_working = self.count + 1
		# elif self.status == "Completed":
		# 	project_id = frappe.get_doc("Project",self.project_id)
		# 	project.total_resources_working = self.count + 1


	def after_save(self):
		self.email_id = self.assignee
		self.send_email()

	def send_email(self):
		frappe.sendmail(recipients="self.email_id",
		subject="Subject of the email",
		message= "Content of the email",
		now=True)
