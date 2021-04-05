// Copyright (c) 2021, Ravi Kharte and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Project', {
// 	// refresh: function(frm) {
//
// 	// }
// });
frappe.ui.form.on("Project", {
  onload: function(frm){
      let is_allowed = frappe.user_roles.includes('System Manager');
      frm.toggle_enable(['title_of_the_project','project_description','start_date','approximate_end_date'], is_allowed);
    },
  onload: function(frm){
        let is_allowed = frappe.user_roles.includes('Manager');
        frm.toggle_enable(['title_of_the_project','project_description','start_date','approximate_end_date'], is_allowed);
      }
});
