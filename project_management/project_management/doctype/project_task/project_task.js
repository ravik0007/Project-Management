// Copyright (c) 2021, Ravi Kharte and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Project Task', {
// 	// refresh: function(frm) {
//
// });
// 	// }
// });

// frappe.ui.form.on("Project Task", { onload:function(frm)
//   {
//     let is_allowed = frappe.user_roles.includes('System Manager');
//     frm.toggle_enable(['status', 'priority'], is_allowed);
//
//   }

frappe.ui.form.on("Project Task", {
  onload: function(frm){
    if (frappe.user_roles.includes('Quality Assurance')) {
      let is_allowed = frappe.user_roles.includes('System Manager');
      frm.toggle_enable(['task_title','start_date','end_date','assignee'], is_allowed);
    } else if (frappe.user_roles.includes('Developer')) {
      let is_allowed = frappe.user_roles.includes('System Manager');
      frm.toggle_enable(['task_title','start_date','end_date'], is_allowed);
    }
  }
});
