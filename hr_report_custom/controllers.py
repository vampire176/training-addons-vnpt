# -*- coding: utf-8 -*-
from openerp import http

# class HrReportCustom(http.Controller):
#     @http.route('/hr_report_custom/hr_report_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_report_custom/hr_report_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_report_custom.listing', {
#             'root': '/hr_report_custom/hr_report_custom',
#             'objects': http.request.env['hr_report_custom.hr_report_custom'].search([]),
#         })

#     @http.route('/hr_report_custom/hr_report_custom/objects/<model("hr_report_custom.hr_report_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_report_custom.object', {
#             'object': obj
#         })