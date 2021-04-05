# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ravi Kharte and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Project(Document):
	def before_save(self):
		self.project_id = self.autoname()

	def autoname(self):
		return self.name
