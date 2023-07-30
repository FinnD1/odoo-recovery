import base64

import xlrd

from odoo import models, fields, api
from odoo.http import request


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many(comodel_name='crm.customer.request', inverse_name='opportunity_id', string='Request')
    sale = fields.Float(string='Sale', compute='total_sale')
    expected_revenue = fields.Char(string='Revenue', compute='compute_revenue')

    # customer_needs=fields.Char()
    import_request = fields.Binary()

    @api.depends('request_ids.qty')
    def total_sale(self):
        for rec in self:
            total_qty = 0
            for record in rec.request_ids:
                total_qty += record.qty
            rec.sale = total_qty

    @api.depends('request_ids.product_id')
    def compute_revenue(self):
        for rec in self:
            total_revenue = 0
            for record in rec.request_ids:
                total_revenue += record.qty * record.product_id.list_price
            rec.expected_revenue = total_revenue

    # @api.model
    # def import_request1(self):
    #     # Xử lý upload file
    #     excel_file = request.httprequest.files.get('file')
    #     # Đọc file
    #     book = xlrd.open_workbook(file_contents=excel_file)
    #     sheet = book.sheet_by_index(0)
    #
    #     for row_no in range(sheet.nrows):
    #         # Lấy dữ liệu từ từng cell trong sheet
    #         product_id = sheet.cell_value(row_no, 1)
    #         opportunity_id = sheet.cell_value(row_no, 2)
    #         date = sheet.cell_value(row_no, 3)
    #         description = sheet.cell_value(row_no, 4)
    #         qty = sheet.cell_value(row_no, 5)
    #
    #         # Tạo crm.lead
    #         self.env['crm.lead'].create({
    #             'product_id': product_id,
    #             'opportunity_id': opportunity_id,
    #             'date': date,
    #             'description': description,
    #             'qty': qty,
    #         })

    # @api.model_create_multi
    # def import_excel(self):
    #     if self.env.context.get('active_id'):
    #         lead = self.env['crm.lead'].browse(self.env.context.get('active_id'))
    #         # Xử lý upload file
    #         file_name = request.httprequest.files.get('file')
    #         # Lấy dữ liệu từ Excel thành JSON
    #         data = excel2json.parse_xls(file_name)
    #         # Tạo các crm.lead từ data
    #         for lead_data in data:
    #             vals = {
    #                 'product_id': lead_data.get('product_id'),
    #                 'opportunity_id': lead_data.get('opportunity_id'),
    #                 'date': lead_data.get('date'),
    #                 'description': lead_data.get('description'),
    #                 'qty': lead_data.get('qty'),
    #             }
    #             # Tạo mới lead
    #             self.env['crm.lead'].create(vals)
    # def import_file(self):
    #     # Decode file
    #     file_data = base64.b64decode(self.file)
    #
    #     # Parse Excel file
    #     workbook = xlrd.open_workbook(file_contents=file_data)
    #     worksheet = workbook.sheet_by_index(0)
    #
    #     # Lặp qua các dòng dữ liệu
    #     for row_num in range(worksheet.nrows):
    #         # Lấy dữ liệu từng cột theo row
    #         vals = {}
    #         row = worksheet.row()
    #
    #         if row[0].value:
    #             vals['product_id'] = row[0].value
    #             vals['opportunity_id'] = row[1].value
    #             vals['date'] = row[2].value
    #             vals['description'] = row[3].value
    #             vals['qty'] = row[4].value
    #
    #         # Tạo record mới trong Odoo
    #         self.env['crm.customer.request'].create({
    #             'product_id': vals['product_id'],
    #             'opportunity_id': vals['opportunity_id'],
    #             'date': vals['date'],
    #             'description': vals['description'],
    #             'qty': vals['qty'],
    #
    #         })
