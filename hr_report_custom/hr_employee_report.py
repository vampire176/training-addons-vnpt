__author__ = 'vampi'
from openerp import tools
from openerp.osv import fields, osv

class hr_employee_report(osv.Model):
    _name = "hr.employee.report"
    _description = "Employee Statistics"
    _auto = False
    _columns = {
        'create_date': fields.datetime('Create Date', readonly=True),
        'department_id': fields.many2one('hr.department', 'Department'),
        'job_id': fields.many2one('hr.job', 'Job Title'),
        'delay_date': fields.float('Delay to Start', digits=(16, 2), readonly=True),
    }
    _order = 'create_date desc'

    _depends = {
        'hr.department': ['id', 'create_date'],
        'hr.employee': ['create_date', 'job_id', 'department_id', 'id','parent_id'],
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'hr_employee_report')
        cr.execute("""
            create or replace view hr_employee_report as (
                 select
                     min(l.id) as id,
                     s.create_date as create_date,
                     s.department_id,
                     s.job_id
                 from
                 hr_department l
                LEFT JOIN
                     hr_employee s on (s.department_id=l.id)
                 GROUP BY
                     s.create_date,
                     s.job_id,
                     s.department_id
            )
        """)
